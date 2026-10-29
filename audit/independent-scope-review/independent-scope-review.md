# Independent scope and counterargument review

Target: S. Boldyrev and N. F. Loureiro, “Tearing-mediated Alfvénic Turbulence in a Relativistic Plasma,” The Astrophysical Journal 979(2), 232 (2025), DOI https://doi.org/10.3847/1538-4357/ada28a.

This is an internal, bounded interpretation review. It does not recommend publication or presume an error. All eleven supplied pages and the complete cached publisher-visible prose were read. The relevant main-text formulas were checked against the cached publisher TeX, and supplied page 4 was inspected visually. Prior-art reading is identified separately below; no full-reading claim is made for the eighteen-page Demidov–Lyubarsky preprint.

## Finding and its strongest benign interpretation

The formal two-parameter window survives the stated reduced-model assumptions. It follows directly from formulas that the source itself prints. The strongest defensible contribution is an explicit domain map distinguishing a first tearing transition from a later prospective current-supply limit. It is not a correction to Eq. (25), a new tearing spectrum, or a demonstration that the source's astrophysical expectation is false.

The source already derives the prospective post-tearing charge-starvation scale in Eq. (25), page 4, right column. The following sentence anticipates that the scale lies below the inertial length in astrophysical applications and conditions the resulting interpretation on that ordering. Any discussion must credit this sentence and Eq. (25). Page 5's broader conclusion should be read together with that qualifier.

There is also an important difference between limits. At fixed fluctuation magnetization, Eq. (25) gives \(a_{\mathrm{ch}}^*/d_{\mathrm{rel}}\to0\) as \(R\to\infty\). The source's expectation is therefore consistent with the ordinary fixed-magnetization, large-scale-separation limit. The formal intermediate window requires a correlated family in which the magnetization grows with \(R\). That double scaling does not contradict the fixed-parameter limit.

## Exact conditional reduction

Write \(R=L_\perp/d_{\mathrm{rel}}>1\), \(x=a/d_{\mathrm{rel}}\), and \(s=\tilde{\sigma}\). For localized profiles, the source's Eqs. (13), (20), (23), and (25) give

\[
\frac{a_t}{d_{\mathrm{rel}}}\sim R^{1/7},\qquad
s\ll R^{5/7},\qquad
\frac{b_a}{b_0}\sim R^{-1/3}x^{5/6},\qquad
\frac{a_{\mathrm{ch}}^*}{d_{\mathrm{rel}}}\sim s^3R^{-2}.
\]

The current-demand proxy from Eq. (14) is

\[
\chi_2(x)=sR^{-2/3}x^{-1/3}.
\]

At the first tearing scale, \(\chi_2(a_t/d_{\mathrm{rel}})=sR^{-5/7}\). Requiring this to be small permits tearing to intervene first. Requiring the same unmodified post-tearing scaling to remain comfortably below the proxy threshold all the way to \(x=1\) instead requires the stronger condition \(s\ll R^{2/3}\). Their difference is the conditional window

\[
R^{2/3}\ll s\ll R^{5/7},
\quad\Longrightarrow\quad
1\ll s^3R^{-2}\ll R^{1/7}.
\]

Thus the interval is a consequence of retained source scalings, fixed density/enthalpy, and treating the proxy threshold as a prospective limit. It is not a solution for the flow after that limit. In contrast, for the Harris profile, source Eq. (21) gives \(\chi_1=sR^{-2/3}\), independent of scale; the positive Harris conclusion is preserved.

The standalone standard-library program in independent-scope-prior-art/stress_test_parameter_window.py checks twenty rational exponents strictly inside the window, four boundary/outside controls, eight finite scale-separation values, six mode-fit identities, and a Harris constant-proxy control. These are scalar/exponent checks, not simulations or a validation of the cascade phenomenology.

## Counterarguments and hidden relations tested

**The interval is asymptotically narrow and sensitive to finite constants.** Its upper/lower magnetization ratio is only \(R^{1/21}\). The largest equal separation from the two bounds is \(R^{1/42}\), attained at \(s=R^{29/42}\). For \(R=10^{12}\), that magnetization margin is approximately 1.93, even though the two midpoint length-scale ratios are approximately 7.20. Two magnetization margins greater than a chosen factor \(K\) require \(R>K^{42}\). Consequently, a formal nonempty interval must not be called a robust, measured astrophysical regime merely because \(R\) is large. Unknown order-one factors can move or eliminate a narrow finite-\(R\) interval. A family \(R=10^{42m}\), \(s=10^{29m}\) is an algebraic witness, not a claim that such systems exist.

**Guide and fluctuation magnetizations are different.** With physical field amplitudes, the source's definitions imply \(s=\sigma(\delta B_0/B_0)^2\). Its strong-guide ordering gives \(s\ll\sigma\), not a universal upper bound \(s\lesssim1\). Choosing a small fixed or shrinking fluctuation/guide ratio and a correspondingly larger guide magnetization is consistent with the printed assumptions. Conversely, an additional fixed upper bound on guide magnetization would eventually exclude the correlated asymptotic family; no such bound is specified in the target. The source reuses magnetic-amplitude notation after introducing a velocity normalization, so cross-paper numerical comparisons should fix physical versus normalized fields explicitly. No dimensional-error claim is made here.

**Fastest-mode fit does not exclude the interval under the same cascade balance.** The source's Appendix Eq. (A19), page 7, gives \(k_{\max}a\sim(d_{\mathrm{rel}}/a)^{1/n}\). If the eddy length along the reconnecting field is inferred from the same nonlinear/tearing-time balance, \(\ell\sim b_a/\gamma_{\max}=a(a/d_{\mathrm{rel}})^{1+1/n}\). Then \(k_{\max}\ell\sim a/d_{\mathrm{rel}}\gg1\). This is a conditional consistency control, not an independently measured eddy geometry. A different finite-length or intermittency model could change it. In the retained \(n=2\) model, the fluctuation amplitude at the prospective crossover scales as \(b_*/b_0\sim R^{(5/2)p-2}\) for \(s=R^p\); its exponent is negative throughout the window, consistent with small transverse bulk velocities under a strong guide.

**Current and density conventions change finite prefactors.** The source prints a current cap \(J<2n|e|c\) on page 4. If its \(n\) is identified with the each-species \(n_0\) in its inertial-length and physical-field magnetization definitions, the squared Ampère-current fraction is \(\chi_2/2\). An exact cap would then move a threshold by an order-one factor and its cube in the crossover length. This observation is conditional on that density identification, not a verified missing factor in a scaling formula. The exponents and asymptotic existence remain unchanged; finite-\(R\) numerical boundaries must not be presented as exact without resolving the conventions.

**The prospective threshold is where the description ceases to be controlled.** The source explicitly states in Section 2.2, page 4, that relativistic bulk parallel current invalidates its nonrelativistic bulk-motion treatment. It discusses possible density variations, acceleration, increased enthalpy/inertial length, and damping. These are serious limitations on extrapolation. They do not algebraically force the prospective threshold below \(d_{\mathrm{rel}}\), but they prevent this calculation from predicting a post-threshold spectrum, dissipation fraction, heating law, or universal arrest. Density compression and scale-dependent heating might move the actual threshold. No source particle data or nonlinear solution is available in this check to decide that issue.

**Optical thinness and small radiation losses require separate physical checks.** The source assumes that radiative effects do not substantially change the cascade, and invokes small Thomson optical depth. Optical thinness alone is not a quantitative guarantee of negligible synchrotron cooling. That point is a limitation of physical realization, not evidence that the algebraic interval is excluded. At fixed dimensionless \(R,\sigma,s,w\), reducing density increases all length scales as \(n_0^{-1/2}\), lowers physical fields as \(n_0^{1/2}\), lowers the Thomson depth as \(n_0^{1/2}\), and increases a synchrotron-cooling/cascade-time ratio as \(n_0^{-1/2}\) under fixed particle energies and geometry. Thus there is no density-independent prohibition in those inequalities alone. This scaling argument does not certify an achievable finite-size astrophysical system: observed system size, field, density, particle distribution and radiative losses must all be specified.

**Distribution-dependent kinetic effects could remove an observational example.** A hard nonthermal spectrum introduces more than one effective particle-inertial/gyro scale. The target represents its plasma with a single enthalpy-dependent inertial length and \(\beta_s=O(1)\). A sufficiently energetic tail, kinetic damping above the presumed cutoff, changing particle moments, or different intermittent current sheets can invalidate that simplified continuation. These are genuine counterarguments to interpreting the formal diagram as a complete physical phase diagram. They are not a demonstrated hidden identity between \(s\) and \(R\) in the target.

## Primary prior art actually read

Ivan Demidov and Yuri Lyubarsky, arXiv:2410.16167v1, submitted 21 October 2024, “Collisionless tearing instability in relativistic non-thermal pair plasma and its application to MHD turbulence”: the official abstract and PDF pages 7–11 were read, covering Section 3.3 and Sections 4.1–4.3, plus the start of Section 5. The full eighteen-page preprint was acquired, but its remaining sections/appendices were not fully read for this assignment. No claim is made about identity with its later ApJ 979, 104 journal version (DOI 10.3847/1538-4357/ad9d3a).

This predecessor already separates tearing onset, the inertial/kinetic cutoff, current supply, and finite scale separation. Its pp. 9–10 include an energy-moment factor \(H=\langle E\rangle\langle E^{-1}\rangle\), and explain when the disruption scale falls too close to or below the effective kinetic cutoff. Page 10 notes how demanding even one decade of a Harris tearing interval is. Page 11 Eq. (41), checked visually, gives a guide-field magnetization threshold with an outer-aspect-ratio factor; rewriting in its own fluctuation magnetization removes that factor and gives an \(R^{2/3}H^{-2/3}\) threshold. Its Eq. (42) concerns distinct intermittent structures. Neither is a direct derivation of the target's localized-profile \(n=2\) post-tearing case. Different enthalpy, density and energy-distribution conventions prevent exact numerical identification without further work. The general competition between current limitation and tearing, and the need to check a kinetic cutoff, must be credited as prior work.

N. F. Loureiro and S. Boldyrev, “Turbulence in Magnetized Pair Plasmas,” ApJL 866(1), L14 (2018), DOI 10.3847/2041-8213/aae483: all five pages of the primary journal PDF held by OSTI were read. Section 3, page 3, already derives the Harris and sinusoidal tearing-mediated scalings and the \(-3\)/\(-8/3\) spectra. Sections 4–5 delimit the low-beta, nonrelativistic model, distinguish the kinetic interval, and caution about finite numerical scale separation and damping. It cannot by itself validate an ultrarelativistic current-cap extrapolation. The later source's formal relation to that prior model is a positive control, not a new phenomenon established by the present scope check.

## Recommendation and unresolved evidence

No stated guide-field, amplitude, mode-fit, density or optical-depth relation was found that universally closes the formal two-parameter window. The narrowness, fixed-parameter limit, order-one constants, kinetic feedback, and the source's explicit page-4 caveat substantially restrict the strength and novelty of a resulting claim. A source-specific domain clarification is supportable; an assertion that the source omitted Eq. (25), proved a false universal astrophysical statement, or predicted a wrong measured spectrum is not supported.

Actual astrophysical occupancy, nonlinear continuation, distribution-dependent damping, and the numerical constants remain unknown. This review does not infer source-author intent and contains no new simulations or author contact. The attached provenance receipt binds exact local source/prior-art bytes and the standalone controls. No manuscript, repository, publication or browser state was changed.
