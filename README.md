---
license: apache-2.0
task_categories:
- text-classification
- feature-extraction
language:
- en
tags:
- synthetic
- decision-support
- advisory
- governance
- insurance
- justice
- explainable-ai
- human-in-the-loop
size_categories:
- n<1K
---

# Decision Evidence Signals v1

## Dataset Summary

**BDR-AI/decision_evidence_signals_v1** is a governed, enterprise-grade synthetic dataset designed to provide structured, explainable, advisory evidence signals that support human decision-making in insurance and justice/regulatory domains.

This dataset contains 300 synthetic records representing various types of evidence signals that may arise during claims review, underwriting, regulatory assessment, and case preparation workflows. Each record provides contextual information about potential areas requiring human professional review.

## Key Characteristics

- ✅ **100% synthetic data** (no real PII, no personal identifiers, no real entities)
- ✅ **Advisory-only signals** (no automated decisions, approvals, or rejections)
- ✅ **Human-in-the-loop by design** (all outputs require professional review)
- ✅ **Governance-first approach** (explicit auditability and compliance)
- ✅ **Production-credible** (realistic but fictional evidence narratives)
- ✅ **Recruiter-safe** (ethical, transparent, and professionally appropriate)

## Dataset Structure

### Data Fields

| Field | Type | Description |
|-------|------|-------------|
| `record_id` | string | Unique identifier (format: REC-XXXXXX) |
| `domain` | string | Domain category: "insurance" or "justice" |
| `use_case` | string | Specific use case within domain |
| `signal_type` | string | Type of evidence signal detected |
| `risk_weight` | string | Risk categorization: "low", "medium", or "high" |
| `evidence_text` | string | Synthetic narrative describing the evidence signal |
| `advisory_note` | string | Explanation of why this signal matters for human review |
| `governance_tag` | string | Fixed value: "advisory_only_human_review_required" |
| `created_at` | string | Synthetic ISO 8601 timestamp |

### Signal Types

The dataset includes six types of evidence signals:

1. **missing_document**: Required documentation not found in submission
2. **document_inconsistency**: Discrepancies between submitted materials
3. **timeline_anomaly**: Unusual temporal patterns or sequences
4. **frequency_anomaly**: Statistical deviations in occurrence rates
5. **policy_conflict**: Potential conflicts with policies or guidelines
6. **prior_reference**: Similarities to historical cases or patterns

### Use Cases

**Insurance Domain:**
- `claims_review`: Evidence signals during claims processing
- `underwriting_support`: Signals for underwriting assessment
- `fraud_triage`: Patterns requiring fraud investigation review

**Justice Domain:**
- `evidence_review`: Signals during evidence examination
- `regulatory_assessment`: Compliance and regulatory review signals
- `case_preparation`: Signals for case preparation workflows

### Data Distribution

- **Total Records**: 300
- **Insurance Records**: 150 (50%)
- **Justice Records**: 150 (50%)
- **Signal Types**: Balanced across all 6 types
- **Risk Weights**: Distributed across low, medium, and high

## Dataset Creation

### Generation Process

This dataset was generated using a controlled synthetic data generation process with:

- **Random seed**: 42 (for reproducibility)
- **Template-based generation**: Evidence narratives created from domain-specific templates
- **Governance validation**: All records validated for compliance before publication
- **No real data sources**: Entirely synthetic, no real-world data used

### Source Code

The complete generation code is available in this repository:
- `generate_dataset.py`: Main generation script
- `validate_dataset.py`: Validation and quality assurance script
- `requirements.txt`: Python dependencies

To regenerate the dataset:

```bash
pip install -r requirements.txt
python generate_dataset.py
python validate_dataset.py
```

## Usage

### Loading the Dataset

**Using Hugging Face Datasets:**

```python
from datasets import load_dataset

# Load dataset
dataset = load_dataset("BDR-AI/decision_evidence_signals_v1")

# Convert to pandas
df = dataset['train'].to_pandas()

print(f"Loaded {len(df)} records")
```

**Using Pandas directly:**

```python
import pandas as pd

# Load from CSV
df = pd.read_csv("decision_evidence_signals_v1.csv")

# Or load from Parquet
df = pd.read_parquet("decision_evidence_signals_v1.parquet")
```

### Example: Filter High-Risk Insurance Signals

```python
# Filter for high-risk insurance signals
high_risk = df[
    (df['domain'] == 'insurance') & 
    (df['risk_weight'] == 'high')
]

print(f"Found {len(high_risk)} high-risk insurance signals")
```

### Example: Analyze Signal Distribution

```python
# Signal type distribution by domain
import pandas as pd

signal_dist = pd.crosstab(
    df['domain'], 
    df['signal_type']
)

print(signal_dist)
```

### Quickstart Notebook

See `quickstart.ipynb` for a comprehensive tutorial covering:
- Loading and exploring the dataset
- Filtering and analysis examples
- Domain and signal type distributions
- Governance verification
- Export and integration patterns

## Intended Use

### ✅ Appropriate Uses

- **Research and Development**: Training advisory AI systems
- **Demonstrations**: Showcasing decision support capabilities
- **Education**: Teaching explainable AI and governance principles
- **Prototyping**: Building human-in-the-loop workflows
- **Testing**: Validating advisory system architectures
- **Benchmarking**: Comparing signal detection approaches

### ❌ Inappropriate Uses

- **Autonomous Decision-Making**: This dataset must NOT be used for automated approvals, rejections, or decisions
- **Production Decisions**: Not suitable for real-world case adjudication without human oversight
- **PII Training**: Do not use to train systems that process real personal data
- **Regulatory Compliance**: Not a substitute for actual compliance frameworks

## Governance Statement

### Advisory-Only Principle

**This dataset does not enable automated decisions.**

All outputs are advisory signals only. Final authority and decision-making responsibility always remain with human professionals. No record in this dataset should be interpreted as a recommendation to approve, reject, or take any specific action.

### Human-in-the-Loop Requirement

Every record includes the governance tag `advisory_only_human_review_required` to explicitly indicate that:

1. Human professional review is mandatory
2. Signals provide context, not conclusions
3. Professional judgment supersedes all algorithmic outputs
4. Accountability remains with human decision-makers

### Synthetic Data Declaration

This dataset contains **100% synthetic data**:

- No real names, locations, organizations, or entities
- No actual case numbers, policy IDs, or reference numbers
- No personal identifiable information (PII)
- All evidence narratives are fictional
- All timestamps are synthetic

### Validation and Auditability

The dataset includes validation scripts (`validate_dataset.py`) that verify:

- Schema compliance
- Governance tag consistency
- Absence of PII patterns
- Prohibition of decision language (approve/reject/deny)
- Data quality standards

## Limitations

### Known Limitations

1. **Synthetic Nature**: While realistic, data does not capture full complexity of real-world cases
2. **Limited Signal Types**: Only 6 signal types; real systems may have dozens
3. **Simple Risk Weights**: Categorical (low/medium/high) rather than continuous scores
4. **No Multi-Signal Records**: Each record represents a single signal type
5. **No Temporal Relationships**: Records are independent, no case progression
6. **English Only**: All text in English, no multilingual support
7. **Domain Scope**: Limited to insurance and justice; not generalizable to all domains

### Bias Considerations

- **Synthetic Bias**: Generation templates may reflect creator assumptions
- **Domain Balance**: 50/50 split may not reflect real-world distribution
- **Signal Balance**: Equal distribution may not match actual occurrence rates
- **Use Case Coverage**: Limited to 3 use cases per domain

## Ethical Considerations

### Responsible AI Principles

This dataset was designed with the following principles:

1. **Transparency**: Full disclosure of synthetic nature and limitations
2. **Accountability**: Clear human-in-the-loop requirements
3. **Privacy**: Zero risk of PII exposure
4. **Fairness**: No real-world bias from actual cases
5. **Safety**: Explicit prohibition on autonomous decision-making

### Misuse Prevention

To prevent misuse:

- Clear governance tags on every record
- Explicit disclaimers in documentation
- Validation scripts to detect compliance violations
- Advisory-only language throughout

## Citation

If you use this dataset in your research or applications, please cite:

### BibTeX

```bibtex
@dataset{bdr_ai_decision_evidence_signals_v1,
  author = {BDR-AI},
  title = {Decision Evidence Signals v1: Synthetic Advisory Dataset for Insurance and Justice Domains},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/datasets/BDR-AI/decision_evidence_signals_v1},
  version = {1.0.0},
  license = {Apache-2.0}
}
```

### APA Style

BDR-AI. (2026). *Decision Evidence Signals v1: Synthetic Advisory Dataset for Insurance and Justice Domains* (Version 1.0.0) [Data set]. Hugging Face. https://huggingface.co/datasets/BDR-AI/decision_evidence_signals_v1

### MLA Style

BDR-AI. "Decision Evidence Signals v1: Synthetic Advisory Dataset for Insurance and Justice Domains." *Hugging Face*, version 1.0.0, 2026, huggingface.co/datasets/BDR-AI/decision_evidence_signals_v1.

## License

This dataset is licensed under the **Apache License 2.0**.

You are free to:
- Use the dataset for any purpose
- Modify and distribute the dataset
- Use in commercial applications

Under the conditions that:
- You provide attribution
- You include the license and copyright notice
- You state any significant changes made

See the [LICENSE](LICENSE) file for full terms.

## Version History

### v1.0.0 (2026-01-06)

- Initial release
- 300 synthetic records
- 2 domains (insurance, justice)
- 6 signal types
- 3 risk weight categories
- Full governance compliance

## Contributing

We welcome contributions that enhance the dataset while maintaining governance standards!

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Contribution guidelines
- Governance principles
- Submission process
- Code of conduct

**Key Requirements for Contributors:**
- Maintain 100% synthetic data (no real PII)
- Preserve advisory-only language
- Include proper governance tags
- Pass validation scripts

## Support and Contact

- **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/BDR-AI/decision_evidence_signals_v1/issues)
- **Discussions**: Ask questions in [Hugging Face Discussions](https://huggingface.co/datasets/BDR-AI/decision_evidence_signals_v1/discussions)
- **Documentation**: See repository files and quickstart notebook

## Acknowledgments

This dataset was created to advance responsible AI practices in decision support systems, with a focus on governance, transparency, and human-centered design.

## Disclaimer

**IMPORTANT**: This dataset provides advisory signals only and is not intended for autonomous decision-making. All outputs require human professional review. The creators and distributors of this dataset assume no liability for decisions made using this data. Users are responsible for ensuring appropriate human oversight and compliance with applicable regulations.

---

**Dataset Version**: 1.0.0  
**Last Updated**: 2026-01-06  
**License**: Apache 2.0  
**Organization**: BDR-AI
