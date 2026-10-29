# Scale ordering in localized tearing-mediated relativistic turbulence

Author: Taylor Kalin.

This computational package classifies scale orderings within the declared
phenomenology of Boldyrev and Loureiro, *Tearing-mediated Alfvénic Turbulence
in a Relativistic Plasma*, ApJ 979, 232 (2025),
[DOI 10.3847/1538-4357/ada28a](https://doi.org/10.3847/1538-4357/ada28a).
It contains original exact exponent calculations and two synthetic figures.
Read [AUDIT_FINDINGS.md](AUDIT_FINDINGS.md) for the reviewed findings and limits.
The finding is a qualified source-specific domain clarification; no core
algebra error is demonstrated. The complete package is published as the
[GitHub audit release v1.0.0](https://github.com/Teylersf/relativistic-tearing-domain-audit/releases/tag/v1.0.0).
[Publication status](PUBLICATION_STATUS.md) records its scope and verification.

```text
python -m pip install -r requirements.txt
python reproduction/run_audit.py
```

See [COMPUTATIONAL_METHODS.md](COMPUTATIONAL_METHODS.md) for the mathematical
definitions and [REPRODUCIBILITY.md](REPRODUCIBILITY.md) for the separate producer
and independent-check runtimes. Programs run offline without source PDFs,
private paths, GPU access or a network service. The producer imports neither
independent verifier. The archived package has passed independent producer,
figure, provenance and scope review; these are internal computational checks.

- `figures/phase-domains.png` distinguishes the two conditional boundaries.
- `figures/current-demand-trajectories.png` shows localized cases with and
  without a secondary crossing, plus a Harris positive control.
- `data/producer-results.json` records exact rational exponents, finite-grid
  checks, transition equalities and the declared formal witnesses.
- `source-provenance.json` records the source-edition identification and limits;
  `audit/` preserves independent review evidence separately from the producer.

The source's paragraph after Eq. (25), p. 4, already expects the secondary
charge-starvation scale to lie below the inertial scale in astrophysical systems
and makes its negligible-starvation conclusion conditional on that expectation.
This package credits that qualification. It does not call Eq. (18) or Eq. (25)
algebraically wrong.

All plotted boundaries use declared unity prefactors. The interval has only a
factor `R^(1/21)` between its magnetization bounds; finite prefactors and actual
plasma constraints can matter. The examples `R=10^(42m)`,
`sigma_tilde=10^(29m)` are formal exponent witnesses, not measured astrophysical
values. A dashed trajectory beyond the current-demand crossing is an algebraic
extrapolation, not a prediction from a valid post-crossing model.

At fixed fluctuation magnetization, the secondary scale instead tends below
the inertial scale as `R` grows, consistently with the source's expectation.
The formal window uses correlated double scaling. Requiring each of its two
magnetization margins to exceed `K` needs `R>K^42`; the diagram is not a
complete physical phase diagram or an inferred astrophysical realization.

No PIC/MHD simulation, new inner-ODE eigenmode reproduction, observed plasma
counterexample, replacement spectrum, reconnection rate or particle-heating
outcome is supplied. Code is [MIT licensed](LICENSE-CODE); original text and
figures are [CC BY 4.0](LICENSE-MANUSCRIPT). Third-party works retain their rights.
