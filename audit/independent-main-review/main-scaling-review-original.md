# Independent main-equation audit

## Scope and positive result

The complete supplied 11-page VOR-formatted paper has been read, including
both captions, footnotes, all appendix subsections and references. All
149 publisher math/tex nodes obtained after normal human clearance were
read; all 78 numbered display equations agree substantively with the
supplied PDF pixels. No new code/field/particle data of the source were
obtained. This note audits the declared main scalings, not full relativistic
kinetics or an original simulation. The separate Appendix audit is pending.

The source's main scaling algebra is largely consistent. In particular:

- The adopted dynamically aligned cascade has b_a proportional to
  a^(1/4) and tau_a proportional to a^(1/2), at fixed outer parameters.
  Combining Eqs.(7),(9),(10) gives Eq.(11), including a_t/d=R^(1/9)
  for n=1 and R^(1/7) for n=2, where R=L_perp/d_rel.
- Substituting Eq.(7) into the declared charge-starvation condition (14)
  gives a_ch/d=R^(-1/3) sigma_tilde^(2/3), Eq.(16). Its ratio to a_t
  and the onset inequality (18) have the printed exponents.
- Constant flux b_a^2 gamma_a, together with the adopted fastest-mode
  scaling, gives b_a/b0=R^(-1/3)(a/d)^h, with
  h=(2n+1)/(3n). A one-dimensional magnetic spectrum then has exponent
  -(2h+1)=-(7n+2)/(3n): -3 for n=1 and -8/3 for n=2. These agree
  with Eqs.(21)-(24) and the abstract.
- The pre-tearing and tearing-mediated amplitudes match at a_t. The
  localized-profile secondary scale in Eq.(25) follows algebraically
  from Eq.(23) and is not a sign or exponent error.

A consistent pair-density convention also passes a factor-of-two control:
if n0 is the density of either species, total matter enthalpy density is
2n0 w m_e c^2. Then the relativistic Alfvén speed is
c/sqrt(1+2/sigma), and the combined pair inertial scale has
d_rel^2=w m_e c^2/(8 pi n0 e^2), exactly the source's definitions. These
factors are not evidence of an automatically incorrect species count.

`verify_main_scalings.py` independently verifies these exponents using
exact Fraction arithmetic and 24 logarithmic model examples. It does
not import source code or solve a fluid/PIC evolution. Figure1 is a
numerical illustration of the inner ODE, while Figure2 is explicitly a
schematic; neither is new PIC evidence in this paper.

## Main conditional gap: onset is not continuation for n=2

There is a genuine distinction between **tearing onset preceding initial
charge starvation** and **charge starvation remaining absent throughout
the subsequent tearing-mediated range**. The former does not imply the
latter for the localized profiles.

Define the source's dimensionless charge parameter at scale a by

    chi(a)=sigma_tilde (b_a/b0)^2 (d/a)^2.

Equation(14) gives charge-starvation onset at chi of order one. In the
tearing-mediated range, the source's own amplitudes imply

    chi(a)=sigma_tilde R^(-2/3)(a/d)^[2(1-n)/(3n)].

For n=1 this is scale independent. The tearing-first condition is
sigma_tilde much smaller than R^(2/3), so chi stays small: the source's
Harris continuation is a positive control.

For n=2,

    chi(a)=sigma_tilde R^(-2/3)(a/d)^(-1/3).

It increases as the cascade moves to smaller a. The initial tearing-first
condition is only sigma_tilde much smaller than R^(5/7). Its later crossing
occurs at

    a_ch*/d = sigma_tilde^3/R^2,                 [source Eq.(25)]

and lies below d only under the additional condition

    sigma_tilde < R^(2/3).

Thus the formally distinct interval

    R^(2/3) << sigma_tilde << R^(5/7)

permits tearing onset first, followed by secondary charge starvation
**above** d. It is not removed by unspecified fixed order-one coefficients.
For a parametric demonstration, set sigma_tilde=R^p with
2/3<p<5/7 and let R grow. Then

    sigma_tilde/R^(5/7) = R^(p-5/7) ->0,
    a_ch*/d = R^(3p-2) ->infinity,
    a_ch*/a_t = R^(3p-15/7) ->0.

All three inequalities are parametrically satisfied. For example p=7/10
has these powers -1/70, +1/10 and -3/70. This is an internal parameter
classification of the declared scalings, not an estimate of R or
sigma_tilde in a real pulsar wind nebula.

The strong-guide assumption does not by itself eliminate that formal
interval: weak fluctuations relative to the guide require
sigma_tilde/sigma_guide much smaller than one, rather than forcing
sigma_tilde below one. A sufficiently larger guide magnetization is
compatible with the ordering. Real radiative/kinetic/size constraints
still require a separate physical parameter analysis, which is not
supplied by these algebraic examples.

### What the source already says

The paragraph immediately after Eq.(25), p.4, explicitly expects this
scale to be below d_rel in astrophysical systems and conditions its
negligible-charge-starvation conclusion on that expectation. That caveat
must be credited. No algebra error is found in Eq.(25), and Eq.(18)
remains a correct **initial onset** comparison.

The potential overreach is the broader abstract/conclusion presentation:
the n=2 onset criterion by itself does not guarantee that charge starvation
is nonessential throughout the tearing-mediated cascade. In particular,
the conclusion p.5 places the spectra and negligible-starvation statement
after Eqs.(27)-(32), without restating the additional Eq.(25) condition.
The repair is a clear two-stage parameter-domain qualification, rather
than declaring the original tearing threshold or spectrum derivation
incorrect.

Under the intermediate condition, the source's k^(-8/3) phenomenology
could apply between a_t and a_ch*, while its assumptions fail at the
secondary crossing. This note does not predict what spectrum or heating
follows. If density, inertial scale, distribution function, damping or
flux changes, the actual evolution may differ. The source itself notes
that heating and kinetic damping alter the charge-starved regime.

## Hard assumptions and non-findings

1. **Profile index.** n=1 and n=2 are adopted asymptotic outer-profile
   classes, not an arbitrary fitted parameter for all possible current
   sheets. A universal claim across all profiles is not demonstrated.
   The positive exponent tests take these classes as stated rather than
   pretending to solve a new outer eigenproblem.
2. **Pressure parameter.** Physical ultrarelativistic applications have
   beta_s of order unity (source p2 discusses isotropic and nearly
   one-dimensional distributions). Appendix A.3's beta_s much less than1
   and A.5's beta_s much greater than1 are expressly formal comparisons to
   nonrelativistic models. The formal large-beta section is not evidence
   that the paper claims a superluminal sound speed for a physical plasma.
3. **Fixed-parameter cascade.** The scalar phase classification assumes
   the source's fixed d_rel, background density and constant-flux/tearing
   scalings up to a crossing. No newly calculated radiation, damping,
   density, heating or guide-field evolution is included.
4. **Frame statement.** A nonzero electric field parallel to the actual
   magnetic field has nonzero invariant E dot B and cannot become zero in
   a frame with E'=0. This supports the qualitative statement in Section
   2.2 when "parallel" means the actual local magnetic field. Merely a
   component along a fixed guide direction would not be the same invariant
   claim; no source numerical implementation of that distinction is
   alleged wrong here.
5. **Normalization notation.** The text introduces velocity-normalized
   magnetic fluctuations and later writes b0 in the fluctuation
   magnetization. Physical versus normalized b0 should be tracked
   carefully if dimensional coefficients are audited. Ratios b_a/b0
   cancel that ambiguity in the present exponent checks. A definitive
   physical-normalization error has not been established here.
6. **Radiation scope.** This paper assumes radiation does not appreciably
   alter its cascade, and separately discusses directional particle
   cooling. A small Thomson optical depth alone is not a cooling-time
   estimate, but no actual source cooling calculation or astrophysical
   parameter set was supplied to test. This is an assumption boundary,
   not a demonstrated physical counterexample.

## Reproduction and limits

Run ordinary Python on `verify_main_scalings.py`. The code uses the
standard library, rejects optimized mode and writes `main-scaling-checks.json`
in this scratch directory. It records both source hashes, all exact
exponents, the parametric intermediate regime and 24 logarithmic
examples. It makes no claim of new code/data by the source authors,
physical bitwise reproducibility, new PIC trajectories or a published
correction. The supplied VOR and publisher equation strings remain
third-party source material.
