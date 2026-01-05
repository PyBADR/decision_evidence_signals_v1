#!/usr/bin/env python3
"""
BDR-AI Decision Evidence Signals Dataset Generator

Generates synthetic, governed advisory evidence signals for insurance and justice domains.
NO REAL DATA. NO PII. ADVISORY ONLY.

Author: BDR-AI
License: Apache 2.0
Date: 2026-01-06
"""

import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Set random seed for reproducibility
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# Configuration
TOTAL_RECORDS = 300
INSURANCE_RATIO = 0.5
OUTPUT_DIR = "."

# Schema definitions
DOMAINS = ["insurance", "justice"]

USE_CASES = {
    "insurance": ["claims_review", "underwriting_support", "fraud_triage"],
    "justice": ["evidence_review", "regulatory_assessment", "case_preparation"]
}

SIGNAL_TYPES = [
    "missing_document",
    "document_inconsistency",
    "timeline_anomaly",
    "frequency_anomaly",
    "policy_conflict",
    "prior_reference"
]

RISK_WEIGHTS = ["low", "medium", "high"]

GOVERNANCE_TAG = "advisory_only_human_review_required"

# Evidence templates by signal type
EVIDENCE_TEMPLATES = {
    "missing_document": [
        "Required documentation for {context} not found in submission package. Standard protocol requires {doc_type} within {timeframe}.",
        "Submission lacks {doc_type} typically provided for {context}. Historical pattern shows {percentage}% inclusion rate.",
        "Expected {doc_type} absent from file. {context} cases normally include this within {timeframe} of initiation."
    ],
    "document_inconsistency": [
        "Discrepancy noted between {doc1} and {doc2}. {field} shows {value1} versus {value2}.",
        "Conflicting information in submitted materials. {doc1} indicates {value1} while {doc2} states {value2}.",
        "Inconsistent {field} across documentation. Primary source shows {value1}, secondary shows {value2}."
    ],
    "timeline_anomaly": [
        "Event sequence shows {event1} occurring {time1} after {event2}, which deviates from typical {timeframe} pattern.",
        "Temporal gap of {duration} between {event1} and {event2} exceeds standard {timeframe} window.",
        "Unusual timing: {event1} recorded {time1} relative to {event2}, outside normal {timeframe} range."
    ],
    "frequency_anomaly": [
        "Pattern shows {count} occurrences of {event} within {timeframe}, compared to baseline average of {baseline}.",
        "Elevated frequency detected: {event} appears {count} times in {timeframe} versus typical {baseline}.",
        "Statistical deviation in {event} frequency. Observed {count} instances against expected {baseline} over {timeframe}."
    ],
    "policy_conflict": [
        "Submitted {item} appears inconsistent with {policy} section {section}. Policy specifies {requirement}.",
        "Potential conflict with {policy} guidelines. {item} may not align with {section} requirements.",
        "Review needed for {policy} compliance. {item} shows characteristics outside {section} parameters."
    ],
    "prior_reference": [
        "Historical record indicates {event} in prior case {case_id} from {timeframe}. Similar pattern to current submission.",
        "Reference to previous matter {case_id} shows comparable {characteristic}. Occurred {timeframe}.",
        "Prior case {case_id} exhibits similar {pattern}. Documented {timeframe} with {outcome} resolution."
    ]
}

ADVISORY_NOTES = {
    "missing_document": [
        "This signal indicates incomplete documentation that may require follow-up to ensure comprehensive review.",
        "Document absence may impact completeness of assessment. Human reviewer should determine if additional materials are needed.",
        "Missing documentation noted for professional review. Reviewer may request supplemental materials if deemed necessary."
    ],
    "document_inconsistency": [
        "Inconsistency flagged for human verification. Professional judgment required to determine materiality and next steps.",
        "Discrepancy identified for expert review. Reviewer should assess whether clarification or correction is warranted.",
        "Conflicting information requires professional evaluation to determine accuracy and appropriate resolution."
    ],
    "timeline_anomaly": [
        "Temporal pattern deviation noted for professional assessment. Reviewer should evaluate whether timing affects case evaluation.",
        "Unusual timeline flagged for expert consideration. Human judgment needed to determine significance.",
        "Timeline variance identified for review. Professional should assess whether sequence impacts case assessment."
    ],
    "frequency_anomaly": [
        "Frequency pattern differs from baseline. Professional review recommended to evaluate significance and context.",
        "Statistical deviation noted for expert assessment. Reviewer should determine if pattern warrants further investigation.",
        "Elevated occurrence rate flagged for human evaluation. Professional judgment required for interpretation."
    ],
    "policy_conflict": [
        "Potential policy alignment issue identified for professional review. Expert should assess compliance and determine appropriate action.",
        "Policy consistency question raised for human evaluation. Reviewer should verify alignment with current guidelines.",
        "Possible guideline conflict noted for expert consideration. Professional judgment required for resolution."
    ],
    "prior_reference": [
        "Historical pattern similarity noted for professional awareness. Reviewer may find prior case context useful for assessment.",
        "Reference to comparable prior matter provided for expert consideration. Professional should evaluate relevance to current case.",
        "Previous case similarity flagged for human review. Expert may wish to examine prior resolution for context."
    ]
}

# Context-specific values for templates
INSURANCE_CONTEXTS = {
    "doc_type": ["incident report", "medical assessment", "repair estimate", "policy verification", "witness statement"],
    "timeframe": ["24 hours", "48 hours", "5 business days", "7 days", "10 business days"],
    "percentage": ["85", "92", "78", "95", "88"],
    "field": ["incident date", "claim amount", "policy number", "location", "description"],
    "event": ["claim submission", "policy modification", "coverage inquiry", "incident report"],
    "policy": ["Standard Coverage Policy", "Claims Handling Guidelines", "Underwriting Manual", "Fraud Prevention Protocol"],
    "section": ["3.2", "5.1", "7.4", "2.8", "4.3"]
}

JUSTICE_CONTEXTS = {
    "doc_type": ["evidence log", "chain of custody form", "witness affidavit", "regulatory filing", "compliance certificate"],
    "timeframe": ["72 hours", "5 business days", "10 days", "14 days", "30 days"],
    "percentage": ["90", "87", "93", "82", "95"],
    "field": ["filing date", "case reference", "jurisdiction", "regulatory code", "submission type"],
    "event": ["regulatory filing", "compliance review", "evidence submission", "case update"],
    "policy": ["Regulatory Compliance Framework", "Evidence Handling Protocol", "Case Management Guidelines", "Administrative Procedures"],
    "section": ["12.3", "8.7", "15.2", "6.4", "9.1"]
}

def generate_evidence_text(signal_type, domain):
    """Generate synthetic evidence text based on signal type and domain."""
    template = random.choice(EVIDENCE_TEMPLATES[signal_type])
    contexts = INSURANCE_CONTEXTS if domain == "insurance" else JUSTICE_CONTEXTS
    
    # Fill template with context-appropriate values
    filled_template = template.format(
        context=random.choice(["this submission", "the case", "this matter", "the file"]),
        doc_type=random.choice(contexts["doc_type"]),
        timeframe=random.choice(contexts["timeframe"]),
        percentage=random.choice(contexts["percentage"]),
        doc1="primary documentation",
        doc2="supplemental materials",
        field=random.choice(contexts["field"]),
        value1="Value A",
        value2="Value B",
        event1="initial submission",
        event2="follow-up documentation",
        time1="3 days",
        duration="12 days",
        count=str(random.randint(4, 8)),
        baseline=str(random.randint(1, 3)),
        event=random.choice(contexts["event"]),
        item="submitted documentation",
        policy=random.choice(contexts["policy"]),
        section=random.choice(contexts["section"]),
        requirement="specific documentation standards",
        case_id=f"REF-{random.randint(100000, 999999)}",
        characteristic="documentation pattern",
        pattern="submission characteristics",
        outcome="standard"
    )
    
    return filled_template

def generate_synthetic_timestamp():
    """Generate synthetic timestamp within the past year."""
    days_ago = random.randint(1, 365)
    timestamp = datetime.now() - timedelta(days=days_ago)
    return timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")

def generate_dataset():
    """Generate the complete synthetic dataset."""
    print(f"Generating {TOTAL_RECORDS} synthetic records...")
    print(f"Random seed: {RANDOM_SEED}")
    
    records = []
    insurance_count = int(TOTAL_RECORDS * INSURANCE_RATIO)
    justice_count = TOTAL_RECORDS - insurance_count
    
    # Generate insurance records
    for i in range(insurance_count):
        domain = "insurance"
        use_case = random.choice(USE_CASES[domain])
        signal_type = random.choice(SIGNAL_TYPES)
        risk_weight = random.choice(RISK_WEIGHTS)
        
        record = {
            "record_id": f"REC-{str(i+1).zfill(6)}",
            "domain": domain,
            "use_case": use_case,
            "signal_type": signal_type,
            "risk_weight": risk_weight,
            "evidence_text": generate_evidence_text(signal_type, domain),
            "advisory_note": random.choice(ADVISORY_NOTES[signal_type]),
            "governance_tag": GOVERNANCE_TAG,
            "created_at": generate_synthetic_timestamp()
        }
        records.append(record)
    
    # Generate justice records
    for i in range(justice_count):
        domain = "justice"
        use_case = random.choice(USE_CASES[domain])
        signal_type = random.choice(SIGNAL_TYPES)
        risk_weight = random.choice(RISK_WEIGHTS)
        
        record = {
            "record_id": f"REC-{str(insurance_count + i + 1).zfill(6)}",
            "domain": domain,
            "use_case": use_case,
            "signal_type": signal_type,
            "risk_weight": risk_weight,
            "evidence_text": generate_evidence_text(signal_type, domain),
            "advisory_note": random.choice(ADVISORY_NOTES[signal_type]),
            "governance_tag": GOVERNANCE_TAG,
            "created_at": generate_synthetic_timestamp()
        }
        records.append(record)
    
    # Create DataFrame
    df = pd.DataFrame(records)
    
    # Shuffle records
    df = df.sample(frac=1, random_state=RANDOM_SEED).reset_index(drop=True)
    
    print(f"\nDataset generated successfully!")
    print(f"Total records: {len(df)}")
    print(f"Insurance records: {len(df[df['domain'] == 'insurance'])}")
    print(f"Justice records: {len(df[df['domain'] == 'justice'])}")
    
    return df

def save_dataset(df):
    """Save dataset in CSV and Parquet formats."""
    csv_path = os.path.join(OUTPUT_DIR, "decision_evidence_signals_v1.csv")
    parquet_path = os.path.join(OUTPUT_DIR, "decision_evidence_signals_v1.parquet")
    
    # Save CSV
    df.to_csv(csv_path, index=False)
    print(f"\nCSV saved to: {csv_path}")
    print(f"CSV size: {os.path.getsize(csv_path) / 1024:.1f} KB")
    
    # Save Parquet
    df.to_parquet(parquet_path, index=False)
    print(f"Parquet saved to: {parquet_path}")
    print(f"Parquet size: {os.path.getsize(parquet_path) / 1024:.1f} KB")
    
    return csv_path, parquet_path

def validate_dataset(df):
    """Perform basic validation checks."""
    print("\n=== VALIDATION CHECKS ===")
    
    # Check for required columns
    required_columns = ["record_id", "domain", "use_case", "signal_type", 
                       "risk_weight", "evidence_text", "advisory_note", 
                       "governance_tag", "created_at"]
    missing_columns = set(required_columns) - set(df.columns)
    if missing_columns:
        print(f"❌ Missing columns: {missing_columns}")
    else:
        print("✅ All required columns present")
    
    # Check for unique record IDs
    if df["record_id"].is_unique:
        print("✅ All record IDs are unique")
    else:
        print("❌ Duplicate record IDs found")
    
    # Check governance tags
    if (df["governance_tag"] == GOVERNANCE_TAG).all():
        print("✅ All governance tags correct")
    else:
        print("❌ Incorrect governance tags found")
    
    # Check domain balance
    insurance_pct = (df["domain"] == "insurance").sum() / len(df) * 100
    justice_pct = (df["domain"] == "justice").sum() / len(df) * 100
    print(f"✅ Domain balance: Insurance {insurance_pct:.1f}%, Justice {justice_pct:.1f}%")
    
    # Check for null values
    null_counts = df.isnull().sum()
    if null_counts.sum() == 0:
        print("✅ No null values found")
    else:
        print(f"❌ Null values found: {null_counts[null_counts > 0]}")
    
    print("\n=== VALIDATION COMPLETE ===")

if __name__ == "__main__":
    print("="*60)
    print("BDR-AI Decision Evidence Signals Dataset Generator")
    print("Version 1.0.0")
    print("="*60)
    
    # Generate dataset
    df = generate_dataset()
    
    # Validate dataset
    validate_dataset(df)
    
    # Save dataset
    save_dataset(df)
    
    # Display sample records
    print("\n=== SAMPLE RECORDS ===")
    print(df.head(3).to_string())
    
    print("\n✅ Dataset generation complete!")
    print("\nNext steps:")
    print("1. Review the generated files")
    print("2. Upload to Hugging Face")
    print("3. Update README.md with citation information")
