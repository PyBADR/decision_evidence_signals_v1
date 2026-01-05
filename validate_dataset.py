#!/usr/bin/env python3
"""
Dataset Validation Script for BDR-AI/decision_evidence_signals_v1

Performs comprehensive validation checks to ensure:
- Schema compliance
- Governance requirements
- Data quality standards
- No PII leakage

Author: BDR-AI
License: Apache 2.0
"""

import pandas as pd
import re
import sys
from pathlib import Path

# Validation configuration
REQUIRED_COLUMNS = [
    "record_id", "domain", "use_case", "signal_type",
    "risk_weight", "evidence_text", "advisory_note",
    "governance_tag", "created_at"
]

VALID_DOMAINS = ["insurance", "justice"]
VALID_SIGNAL_TYPES = [
    "missing_document", "document_inconsistency", "timeline_anomaly",
    "frequency_anomaly", "policy_conflict", "prior_reference"
]
VALID_RISK_WEIGHTS = ["low", "medium", "high"]
REQUIRED_GOVERNANCE_TAG = "advisory_only_human_review_required"

# PII detection patterns (basic)
PII_PATTERNS = {
    "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
    "phone": r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b",
    "ssn": r"\b\d{3}-\d{2}-\d{4}\b",
    "credit_card": r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b"
}

# Prohibited decision language
PROHIBITED_TERMS = [
    "approve", "approved", "reject", "rejected", "deny", "denied",
    "accept", "accepted", "decline", "declined", "authorize", "authorized",
    "must approve", "must reject", "automatically", "final decision"
]

class DatasetValidator:
    def __init__(self, csv_path):
        self.csv_path = Path(csv_path)
        self.df = None
        self.errors = []
        self.warnings = []
        self.passed = []
        
    def load_dataset(self):
        """Load the dataset from CSV."""
        try:
            self.df = pd.read_csv(self.csv_path)
            self.passed.append(f"Dataset loaded successfully: {len(self.df)} records")
            return True
        except Exception as e:
            self.errors.append(f"Failed to load dataset: {e}")
            return False
    
    def validate_schema(self):
        """Validate dataset schema."""
        print("\n[1/8] Validating schema...")
        
        # Check required columns
        missing_cols = set(REQUIRED_COLUMNS) - set(self.df.columns)
        if missing_cols:
            self.errors.append(f"Missing required columns: {missing_cols}")
        else:
            self.passed.append("All required columns present")
        
        # Check for extra columns
        extra_cols = set(self.df.columns) - set(REQUIRED_COLUMNS)
        if extra_cols:
            self.warnings.append(f"Extra columns found: {extra_cols}")
    
    def validate_record_ids(self):
        """Validate record ID uniqueness and format."""
        print("[2/8] Validating record IDs...")
        
        # Check uniqueness
        if self.df["record_id"].is_unique:
            self.passed.append("All record IDs are unique")
        else:
            duplicates = self.df[self.df["record_id"].duplicated()]["record_id"].tolist()
            self.errors.append(f"Duplicate record IDs found: {duplicates[:5]}...")
        
        # Check format (REC-XXXXXX)
        invalid_ids = self.df[~self.df["record_id"].str.match(r"^REC-\d{6}$")]
        if len(invalid_ids) > 0:
            self.errors.append(f"Invalid record ID format: {invalid_ids['record_id'].tolist()[:5]}")
        else:
            self.passed.append("All record IDs follow correct format (REC-XXXXXX)")
    
    def validate_enums(self):
        """Validate enumerated fields."""
        print("[3/8] Validating enumerated fields...")
        
        # Validate domains
        invalid_domains = self.df[~self.df["domain"].isin(VALID_DOMAINS)]
        if len(invalid_domains) > 0:
            self.errors.append(f"Invalid domains found: {invalid_domains['domain'].unique()}")
        else:
            self.passed.append("All domains are valid")
        
        # Validate signal types
        invalid_signals = self.df[~self.df["signal_type"].isin(VALID_SIGNAL_TYPES)]
        if len(invalid_signals) > 0:
            self.errors.append(f"Invalid signal types: {invalid_signals['signal_type'].unique()}")
        else:
            self.passed.append("All signal types are valid")
        
        # Validate risk weights
        invalid_risks = self.df[~self.df["risk_weight"].isin(VALID_RISK_WEIGHTS)]
        if len(invalid_risks) > 0:
            self.errors.append(f"Invalid risk weights: {invalid_risks['risk_weight'].unique()}")
        else:
            self.passed.append("All risk weights are valid")
    
    def validate_governance(self):
        """Validate governance requirements."""
        print("[4/8] Validating governance compliance...")
        
        # Check governance tags
        incorrect_tags = self.df[self.df["governance_tag"] != REQUIRED_GOVERNANCE_TAG]
        if len(incorrect_tags) > 0:
            self.errors.append(f"Incorrect governance tags: {len(incorrect_tags)} records")
        else:
            self.passed.append(f"All {len(self.df)} records have correct governance tag")
        
        # Check for prohibited decision language
        text_columns = ["evidence_text", "advisory_note"]
        for col in text_columns:
            for term in PROHIBITED_TERMS:
                matches = self.df[self.df[col].str.lower().str.contains(term, na=False)]
                if len(matches) > 0:
                    self.errors.append(f"Prohibited term '{term}' found in {col}: {len(matches)} records")
        
        if not any("Prohibited term" in e for e in self.errors):
            self.passed.append("No prohibited decision language found")
    
    def validate_pii(self):
        """Check for potential PII leakage."""
        print("[5/8] Scanning for PII...")
        
        text_columns = ["evidence_text", "advisory_note"]
        pii_found = False
        
        for col in text_columns:
            for pii_type, pattern in PII_PATTERNS.items():
                matches = self.df[self.df[col].str.contains(pattern, regex=True, na=False)]
                if len(matches) > 0:
                    self.errors.append(f"Potential {pii_type} found in {col}: {len(matches)} records")
                    pii_found = True
        
        if not pii_found:
            self.passed.append("No PII patterns detected")
    
    def validate_data_quality(self):
        """Validate data quality metrics."""
        print("[6/8] Validating data quality...")
        
        # Check for null values
        null_counts = self.df.isnull().sum()
        if null_counts.sum() > 0:
            self.errors.append(f"Null values found: {null_counts[null_counts > 0].to_dict()}")
        else:
            self.passed.append("No null values found")
        
        # Check for empty strings
        text_columns = ["evidence_text", "advisory_note"]
        for col in text_columns:
            empty = self.df[self.df[col].str.strip() == ""]
            if len(empty) > 0:
                self.errors.append(f"Empty strings in {col}: {len(empty)} records")
        
        # Check text length minimums
        for col in text_columns:
            too_short = self.df[self.df[col].str.len() < 20]
            if len(too_short) > 0:
                self.warnings.append(f"Very short text in {col}: {len(too_short)} records < 20 chars")
    
    def validate_distribution(self):
        """Validate data distribution and balance."""
        print("[7/8] Validating data distribution...")
        
        # Domain balance
        domain_counts = self.df["domain"].value_counts()
        insurance_pct = domain_counts.get("insurance", 0) / len(self.df) * 100
        justice_pct = domain_counts.get("justice", 0) / len(self.df) * 100
        
        if abs(insurance_pct - 50) > 5:  # Allow 5% tolerance
            self.warnings.append(f"Domain imbalance: Insurance {insurance_pct:.1f}%, Justice {justice_pct:.1f}%")
        else:
            self.passed.append(f"Domain balance acceptable: Insurance {insurance_pct:.1f}%, Justice {justice_pct:.1f}%")
        
        # Signal type distribution
        signal_counts = self.df["signal_type"].value_counts()
        min_count = signal_counts.min()
        max_count = signal_counts.max()
        if max_count > min_count * 2:  # Check for severe imbalance
            self.warnings.append(f"Signal type imbalance detected (min: {min_count}, max: {max_count})")
        else:
            self.passed.append("Signal type distribution acceptable")
    
    def validate_timestamps(self):
        """Validate timestamp format and values."""
        print("[8/8] Validating timestamps...")
        
        try:
            # Try to parse timestamps
            pd.to_datetime(self.df["created_at"])
            self.passed.append("All timestamps are valid ISO 8601 format")
        except Exception as e:
            self.errors.append(f"Invalid timestamp format: {e}")
    
    def generate_report(self):
        """Generate validation report."""
        print("\n" + "="*70)
        print("VALIDATION REPORT")
        print("="*70)
        
        print(f"\nDataset: {self.csv_path}")
        print(f"Total Records: {len(self.df) if self.df is not None else 0}")
        
        print(f"\n✅ PASSED CHECKS ({len(self.passed)}):")
        for check in self.passed:
            print(f"  ✓ {check}")
        
        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  ! {warning}")
        
        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)}):")
            for error in self.errors:
                print(f"  ✗ {error}")
        
        print("\n" + "="*70)
        
        if self.errors:
            print("RESULT: VALIDATION FAILED")
            print("="*70)
            return False
        elif self.warnings:
            print("RESULT: VALIDATION PASSED WITH WARNINGS")
            print("="*70)
            return True
        else:
            print("RESULT: VALIDATION PASSED")
            print("="*70)
            return True
    
    def run_all_validations(self):
        """Run all validation checks."""
        print("\nStarting comprehensive dataset validation...")
        
        if not self.load_dataset():
            return False
        
        self.validate_schema()
        self.validate_record_ids()
        self.validate_enums()
        self.validate_governance()
        self.validate_pii()
        self.validate_data_quality()
        self.validate_distribution()
        self.validate_timestamps()
        
        return self.generate_report()

if __name__ == "__main__":
    # Default to current directory
    csv_path = "decision_evidence_signals_v1.csv"
    
    if len(sys.argv) > 1:
        csv_path = sys.argv[1]
    
    validator = DatasetValidator(csv_path)
    success = validator.run_all_validations()
    
    sys.exit(0 if success else 1)
