# Computational methods and limits

Author: Taylor Kalin.

Write `R=L_perp/d_rel>1`, `x=a/d_rel`, and let `sigma_tilde` be the source's
fluctuation magnetization. The two adopted profile indices are `n=1` (Harris)
and `n=2` (localized); no new profile or outer eigenproblem is solved.

Combining the source's aligned-cascade turnover time with its fastest tearing
rate gives `x_t=R^[n/(4+5n)]`. Combining the pre-tearing amplitude with its
current-demand condition gives `x_ch=R^(-1/3)*sigma_tilde^(2/3)` for an
**unmodified** cascade. These are source Eqs. (7), (9)–(20), pp. 3–4.

Constant flux in the adopted tearing range gives
`b_a/b0=R^(-1/3)*x^h`, `h=(2n+1)/(3n)`, and the one-dimensional spectrum
exponent `-(7n+2)/(3n)`. The pre-tearing and tearing-range amplitudes match at
`x_t`. The source current-demand diagnostic then becomes

```text
C(x)=sigma_tilde*(b_a/b0)^2*x^-2
    =sigma_tilde*R^(-2/3)*x^[-2(n-1)/(3n)].
```

For Harris profiles it is constant: tearing first below its `R^(2/3)`
magnetization threshold also keeps this diagnostic below unity throughout the
continued range. For localized profiles it increases as `x` decreases.
The source's own Eq. (25) is `x_star=sigma_tilde^3/R^2`. Thus initial tearing
before the unmodified current-demand crossing uses the weaker threshold
`sigma_tilde<R^(5/7)`, while `x_star<1` requires `sigma_tilde<R^(2/3)`.
These classify conditional continuations; they do not specify physical
post-threshold evolution. The source's paragraph following Eq. (25) already
states its astrophysical expectation that `x_star<1`, and that qualification
is retained.

Every scale prefactor omitted by the source's scaling notation is set to unity
only to define the displayed synthetic boundaries. Equality is an illustrative
boundary, not an asymptotically separated regime. The original `<<` conditions
require separation from it. The localized interval spans only `R^(1/21)` in
magnetization; at its geometric midpoint each margin is `R^(1/42)`. This is
about 1.93 for `R=10^12`, so finite coefficients cannot be dismissed in an
ordinary finite example.
Both magnetization margins greater than `K` require `R>K^42`.
At fixed `sigma_tilde`, `x_star=sigma_tilde^3/R^2` tends to zero as `R`
grows. The formal intermediate family below instead correlates magnetization
with scale separation; it does not contradict that fixed-parameter limit.

All scientific arithmetic uses exact `fractions.Fraction`. Input parameters are
represented by rational `log10(R)` and `log10(sigma_tilde)`; the code never
exponentiates their enormous formal values. It checks 144 finite log-coordinate
examples: both indices, `log10(R)=3,6,12,30,42,84,126,210`, and
`sigma_tilde=R^p` for `p=-1/10,0,1/3,3/5,2/3,29/42,5/7,4/5,1`. The 24
threshold-equality cases are recorded separately. Invalid initial post-tearing
conditions are classified rather than silently extrapolated as valid branches.
An unmodified-cascade `x_ch<1` is only an algebraic extrapolation; source
footnote 4 assumes that scale exceeds the inertial scale in its discussion.

Three formal witnesses use `R=10^(42m)`, `sigma_tilde=10^(29m)`, `m=1,2,3`.
They give exact log-scale identities:

```text
log10(x_t)=6m,             log10(x_star)=3m,
log10(C_at_onset)=-m,      log10(C_at_d_if_continued)=m,
log10(x_star/x_t)=-3m.
```

Each magnetization margin is `10^m`. Extending the integer family makes the
onset diagnostic tend to zero while the two scale gaps grow. These are
parametric consistency examples, not measured astrophysical values or a proof
of every physical admissibility condition.

Figure 1 plots log-coordinate phase bounds and these witnesses. Figure 2 fixes
`log10(R)=42`; its localized paths use `log10(sigma_tilde)=26,29`, and the
Harris control uses 26, below its own initial threshold. The localized crossing
is `x_star=10^3`. Solid curves stop or remain below the current-demand boundary;
the dashed segment is explicitly a formal continuation after that boundary.
Changing density, inertial scale, damping, radiative losses, cascade flux or
particle distributions can change the physical problem. None is evolved here.

Separate independent programs retain the main scaling controls and Appendix
algebra/special-function controls. The latter passed; no new full inner-ODE
reconstruction is added. They are independent implementations and are never
imported into the original producer. Copied original notes/results and explicit
portability adaptations must be distinguished from a newly rerun receipt.
