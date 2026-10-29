# Reproduction

Author: Taylor Kalin.

The original plotting producer uses CPython 3.12.14, NumPy 2.3.5 and
Matplotlib 3.11.2. Its algebra uses only exact standard-library fractions;
floating point is restricted to figure coordinates and drawing. Install
`requirements.txt` in that environment and run:

```text
python reproduction/run_audit.py
```

Use ordinary Python without `-O`. The producer rejects optimized mode before
writing scientific outputs. `--output-root` can direct all generated data and
figures into another folder. Source PDFs and network access are unnecessary.

The separate independent checks use CPython 3.13.7. The main exponent and scope
verifiers use only the Python standard library. The Appendix verifier additionally uses
mpmath 1.3.0 at 80 decimal digits. Install `requirements-verifiers.txt` in the
independent environment and run:

```text
python audit/independent-main-review/verify_main_scalings.py
python audit/independent-appendix-review/check_appendix_independently.py
python audit/independent-scope-review/stress_test_parameter_window.py
```

The copied verifiers use recorded source provenance when source PDFs are absent;
they do not assert that missing PDFs were rehashed. Original scripts, original
receipts and the explicit adaptation record are retained separately. No verifier
imports the producer, and the producer imports no verifier. The two actual
environments are recorded separately; a combined environment is not claimed.
Original review notes describe their original source/scratch runs. The portable
Appendix JSON omits its original wall-clock field so that its scientific output
is deterministic; the actual new run time remains in `data/independent-portability.json`.

Recorded figures can reproduce byte for byte in the stated plotting environment.
Fonts/PNG encoding may differ elsewhere. Exact exponent identities are not a
claim of cross-platform bitwise figure identity, astrophysical validity,
independent human peer review or a source-simulation reproduction. The package
is published as a reproducible GitHub audit report, with assessment
`qualified_or_inconclusive_findings`. No correction-paper, PDF, DOI or formal
venue submission is part of this release. The byte manifest lists every initial
release file except itself; later public availability proofs under `publication/`
are explicitly outside that frozen manifest. Git staging preserves raw bytes,
and each staged blob is checked against disk before the release commit.
