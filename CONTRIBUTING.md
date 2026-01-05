# Contributing to BDR-AI/decision_evidence_signals_v1

Thank you for your interest in contributing to the Decision Evidence Signals dataset! This document provides guidelines for contributing to this project.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How to Contribute](#how-to-contribute)
3. [Governance Principles](#governance-principles)
4. [Contribution Types](#contribution-types)
5. [Submission Guidelines](#submission-guidelines)
6. [Review Process](#review-process)

---

## Code of Conduct

### Our Standards

This project is committed to:

- **Ethical AI**: All contributions must align with responsible AI principles
- **Transparency**: Clear documentation and explainable processes
- **Privacy**: Absolute prohibition on real data or PII
- **Human-Centric**: Advisory-only outputs, never autonomous decisions
- **Inclusivity**: Respectful collaboration and diverse perspectives

### Unacceptable Behavior

- Introducing real data, PII, or personal identifiers
- Adding automated decision logic or approval/rejection mechanisms
- Harassment, discrimination, or unprofessional conduct
- Violating governance principles outlined in the dataset card

---

## How to Contribute

### Getting Started

1. **Review the Dataset**: Familiarize yourself with the current dataset structure and documentation
2. **Check Issues**: Look for open issues or discussions that interest you
3. **Propose Changes**: Open an issue to discuss significant changes before implementing
4. **Follow Guidelines**: Ensure your contribution aligns with governance principles

### Areas for Contribution

- **Dataset Enhancement**: Propose new signal types or use cases
- **Documentation**: Improve README, tutorials, or examples
- **Code Quality**: Enhance generation or validation scripts
- **Testing**: Add validation checks or quality assurance tests
- **Examples**: Create usage examples, notebooks, or integration guides
- **Bug Fixes**: Report or fix issues in existing code or data

---

## Governance Principles

### Non-Negotiable Requirements

All contributions MUST:

1. **Use Synthetic Data Only**
   - No real names, locations, organizations, or identifiers
   - No actual case numbers, policy IDs, or reference numbers
   - All data must be clearly fictional

2. **Maintain Advisory-Only Language**
   - No "approve", "reject", "deny", "authorize" language
   - No automated decision instructions
   - All outputs must require human review

3. **Include Governance Tags**
   - All records must have `governance_tag: "advisory_only_human_review_required"`
   - No exceptions

4. **Preserve Human-in-the-Loop**
   - Dataset must not enable autonomous decision-making
   - Clear disclaimers required
   - Professional judgment always required

### Validation Requirements

Before submitting:

- Run `validate_dataset.py` to ensure compliance
- Verify no PII patterns detected
- Confirm governance tags are correct
- Check schema compliance

---

## Contribution Types

### 1. Dataset Enhancements

**Adding New Signal Types:**

```python
# Propose new signal type with:
- Signal type name (e.g., "regulatory_threshold_proximity")
- Description and use cases
- Example evidence templates
- Advisory note templates
- Rationale for inclusion
```

**Expanding Use Cases:**

- Propose new use cases for existing domains
- Provide context and examples
- Ensure alignment with domain (insurance/justice)

**Adding Metadata Fields:**

- Propose new fields with clear purpose
- Provide schema definition
- Include generation logic
- Maintain backward compatibility

### 2. Documentation Improvements

**README Updates:**

- Clarify existing sections
- Add usage examples
- Improve governance explanations
- Fix typos or formatting

**Tutorial Creation:**

- Jupyter notebooks demonstrating specific use cases
- Integration guides for popular frameworks
- Best practices documentation

### 3. Code Contributions

**Generation Script:**

- Improve randomization logic
- Add new evidence templates
- Enhance configurability
- Optimize performance

**Validation Script:**

- Add new validation checks
- Improve PII detection
- Enhance reporting
- Add automated tests

### 4. Quality Assurance

**Testing:**

- Unit tests for generation logic
- Integration tests for data loading
- Validation test suites
- Performance benchmarks

**Bug Reports:**

- Clear description of issue
- Steps to reproduce
- Expected vs. actual behavior
- Environment details

---

## Submission Guidelines

### Issue Submission

**Bug Reports:**

```markdown
**Description**: Clear description of the bug
**Steps to Reproduce**: 
1. Step one
2. Step two
**Expected Behavior**: What should happen
**Actual Behavior**: What actually happens
**Environment**: Python version, OS, package versions
**Additional Context**: Screenshots, logs, etc.
```

**Feature Requests:**

```markdown
**Feature Description**: What you want to add
**Use Case**: Why this is valuable
**Governance Compliance**: How it aligns with principles
**Implementation Ideas**: Proposed approach (optional)
**Alternatives Considered**: Other options explored
```

### Pull Request Process

1. **Fork the Repository**
   - Create a personal fork
   - Clone to your local machine

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**
   - Follow coding standards
   - Add tests if applicable
   - Update documentation

4. **Run Validation**
   ```bash
   python validate_dataset.py
   ```

5. **Commit Changes**
   ```bash
   git commit -m "feat: clear description of changes"
   ```
   
   Use conventional commits:
   - `feat:` New feature
   - `fix:` Bug fix
   - `docs:` Documentation
   - `test:` Testing
   - `refactor:` Code refactoring

6. **Push to Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open Pull Request**
   - Clear title and description
   - Reference related issues
   - Explain changes and rationale
   - Include validation results

### Pull Request Template

```markdown
## Description
[Clear description of changes]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Other (specify)

## Governance Compliance
- [ ] No real data or PII introduced
- [ ] Advisory-only language maintained
- [ ] Governance tags correct
- [ ] Validation script passes
- [ ] Documentation updated

## Testing
- [ ] Validation script run successfully
- [ ] Manual testing completed
- [ ] No regressions introduced

## Related Issues
Closes #[issue number]

## Additional Notes
[Any additional context]
```

---

## Review Process

### Review Criteria

Contributions will be evaluated on:

1. **Governance Compliance**: Strict adherence to principles
2. **Code Quality**: Clean, documented, maintainable code
3. **Documentation**: Clear explanations and examples
4. **Testing**: Adequate validation and testing
5. **Value**: Meaningful improvement to the dataset

### Review Timeline

- **Initial Response**: Within 3-5 business days
- **Full Review**: Within 1-2 weeks
- **Revisions**: Iterative feedback as needed

### Approval Process

1. **Automated Checks**: Validation scripts must pass
2. **Maintainer Review**: Manual review by project maintainers
3. **Governance Review**: Verification of compliance
4. **Merge**: Approved contributions merged to main branch

---

## Development Setup

### Prerequisites

- Python 3.9+
- Git
- Virtual environment tool (venv, conda, etc.)

### Local Setup

```bash
# Clone repository
git clone https://github.com/BDR-AI/decision_evidence_signals_v1.git
cd decision_evidence_signals_v1

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run generation script
python generate_dataset.py

# Run validation
python validate_dataset.py
```

### Running Tests

```bash
# Validate dataset
python validate_dataset.py decision_evidence_signals_v1.csv

# Check for PII
grep -i "@" decision_evidence_signals_v1.csv  # Should return nothing

# Verify governance tags
grep -v "advisory_only_human_review_required" decision_evidence_signals_v1.csv | wc -l  # Should be 1 (header only)
```

---

## Questions or Help?

- **Discussions**: Use GitHub Discussions for questions
- **Issues**: Report bugs or request features via Issues
- **Hugging Face**: Comment on the dataset page for dataset-specific questions

---

## License

By contributing, you agree that your contributions will be licensed under the Apache 2.0 License.

---

## Acknowledgments

We appreciate all contributions that help make this dataset more valuable while maintaining the highest standards of governance and ethical AI practices.

Thank you for contributing responsibly! 🙏
