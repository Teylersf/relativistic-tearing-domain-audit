# Independent Appendix A check

Target: Boldyrev and Loureiro, *Tearing-mediated Alfvénic Turbulence in a Relativistic Plasma*, ApJ 979, 232 (2025), DOI 10.3847/1538-4357/ada28a.

Scope: Appendix A1–A45, supplied PDF pp. 5–10, with the exact publisher-browser mathematical nodes as a second transcription source. The setup on pp. 1–3 and the Appendix introduction were read for notation. This is not a new full-paper, source-code or simulation reproduction. The supplied PDF was hashed locally; no fresh publisher PDF was acquired, so fresh-PDF byte identity is not asserted. No network, contact, Git mutation or publication action was performed.

## Outcome

The main Appendix reductions, matching constants, pressure-branch integral and hypergeometric transformation pass the independent checks below. I found no demonstrated substantive algebraic contradiction in A1–A45. The strict ordering and uniformity qualifications below should accompany quantitative use of the asymptotic formulas. They are not evidence that the paper's leading fastest-mode scalings are wrong.

Use \(\epsilon=d_{\rm rel}/a\), \(B=\beta_s>0\), \(Y=\phi'\), and \(\lambda>0\). This \(\epsilon\) denotes the inertial-to-sheet ratio, not the source's separate \(ka\) notation. A prime on \(Y\) refers to \(\xi\); on a hypergeometric function it refers to its argument.

## 1. A1–A5: the integration and matching condition are consistent

After eliminating \(\psi''=-\lambda\phi''/\xi\) with A2, the A1 residual is

\[
R_1=\lambda\psi-\xi\phi+\epsilon^2
(\lambda^2/\xi+B^2\xi)\phi''.
\]

Direct differentiation gives

\[
\xi R_1''=\frac{d}{d\xi}\left[
\epsilon^2(\lambda^2+B^2\xi^2)Y''
-\frac{2\lambda^2\epsilon^2}{\xi}Y'
-(\lambda^2+\xi^2)Y\right].
\]

Thus A3 follows by integration; the sign and the \(2\lambda^2/\xi\) term are correct. In the outer matching limit, \(\lambda\psi\simeq\xi\phi\) with normalized \(\psi_{\rm out}(0)=1\) gives \(Y\simeq-\lambda/\xi^2\), hence the integration constant \(C=\lambda\) used in A5. It is not an arbitrary additional spatial freedom after outer matching.

A2 also gives directly

\[
\int\frac{Y'}{\xi}\,d\xi=-\lambda^{-1}\int\psi''\,d\xi
=-\Delta'/\lambda,
\]

which is A4 with the stated normalization. The infinite limits are those of a matched inner calculation, not literal permission to apply the linearized magnetic profile beyond its domain at finite sheet width.

## 2. A7–A16 and A23: inner solution, overlap and coefficient

Differentiation of A8 gives

\[
Y_I'=-\frac{\lambda\xi}{\epsilon^2(\lambda^2+B^2\xi^2)}.
\]

Substitution into A7 gives exactly its right-hand side \(\lambda\). The integral used in the leading matching calculation is

\[
\int_{-\infty}^{\infty}\frac{Y_I'}{\xi}\,d\xi
=-\frac{\pi}{B\epsilon^2},\qquad
\lambda=\frac{B\epsilon^2\Delta'}{\pi}.
\]

Therefore A16 is the \(B=1\) instance of A23. No sign or missing factor of two was found. This is a coefficient of the displayed leading inner approximation. It is not an exact finite-parameter eigenvalue calculation of A5.

The A10-to-A12 rearrangement is also correct: in \(u=\xi/(B\epsilon)\), its exponential-integral constant is \(\int_0^\infty e^{-v}\ln v\,dv=-\gamma_0\). Writing \(q=\lambda/(B^2\epsilon^2)\), A12 has the small-\(u\) expansion

\[
Y_{II}=-q\ln u+(C_{II}-\gamma_0q/2)
+(-C_{II}-\gamma_0q/2)u+O(u^2\ln u).
\]

Matching its constant and linear terms to A8 gives exactly

\[
C_{II}=-\gamma_0q/2,\qquad
C_I=q[\ln(B^2\epsilon/\lambda)-\gamma_0],
\]

the printed A13–A14. For the paper's Fig. 1 parameters \(B=1\), \(\epsilon=10^{-2}\), \(\lambda=10^{-4}\), the constant is about 4.028; the nominal overlap is \(10^{-4}\ll\xi\ll10^{-2}\), consistent with the plotted illustration. I have not recreated the plotted full-ODE solution.

The strict overlap condition is

\[
\lambda/B\ll B\epsilon,\qquad
\lambda\ll B^2\epsilon.
\]

In the small-\(B\) pressure branch, A23 turns this into \(\epsilon\Delta'\ll B\), up to the stated coefficient. A25/A28 correctly identify the order-of-magnitude crossover. A numerical use of the \(1/\pi\) coefficient close to that crossover requires an error analysis; \(\lesssim\) is not itself a strict asymptotic overlap. The pressureless and pressure-containing scalings A21/A23 agree in order at \(\epsilon\Delta'\sim B\). The \(\delta\) of A6 and the explicitly separately named \(\delta_0\) of A26 should not be silently identified as a single uniquely defined layer width.

## 3. A17–A29: the fastest-mode scalings are preserved

Using \(\lambda=\gamma/(kb_a)\) and \(\Delta'\propto(ka)^{-n}\) in A16 gives A18. Setting \(\lambda\sim\epsilon\) gives \(k_{\max}a\sim\epsilon^{1/n}\), and then

\[
\gamma_{\max}\sim(b_a/a)\epsilon^{1+1/n},
\]

which is A19–A20. The low-pressure crossover in A25/A28 does not change this leading maximum. A21 and A23 are different small-\(\Delta'\) regimes, not identical dispersion relations for arbitrary \(\Delta'\).

## 4. A30–A40: the hypergeometric reduction checks

Set \(h=Y+1/\lambda\), \(z=-B^2\xi^2/\lambda^2\), and \(r=\lambda^2/(B^2\epsilon^2)\). Direct chain-rule substitution into A30 yields

\[
z(1-z)h_{zz}-\tfrac12(1+z)h_z+\tfrac14r h=0,
\]

exactly A31. The A33 parameters obey \(\alpha+\beta_h=-1/2\), \(\alpha\beta_h=-r/4\), \(\gamma_h=-1/2\). In particular,

\[
\alpha\beta_h/\gamma_h=r/2
\]

is exact, not merely a small-\(\alpha\) approximation. It reduces the prefactor in A35 to \(-\widetilde C_I/\epsilon^2\). Therefore A38 follows from the retained \(1/(1-z)\) part of A37 with the stated sign and normalization.

The A36 connection identity agrees numerically with direct \({}_2F_1\) evaluation on the physical negative-real-\(z\) branch. The large-argument coefficients used in A39 also follow from the connection coefficients:

\[
\frac{\Gamma(-1/2)\Gamma(-1/2-2\alpha)}
{\Gamma(-1/2-\alpha)^2}=1+O(\alpha^2),
\]

\[
\frac{\Gamma(-1/2)\Gamma(1/2+2\alpha)}{\Gamma(\alpha)^2}
=-2\pi\alpha^2[1+O(\alpha)].
\]

Expanding \((-z)^{-\alpha}\) then gives A39 and A40. It additionally requires \(|\alpha\ln(-z)|\ll1\) when the linearized logarithm is used. For real positive \(\xi\), \(z<0\); the prose twice calling the large-argument regime \(z\gg1\) on p. 9 should be read as \(|z|\gg1\). The displayed \((-z)\) formulas themselves use the appropriate branch. This is a directional prose issue, not a demonstrated error in the result.

## 5. A37/A41–A45: bounded uniformity cautions, not a refutation

The source explicitly acknowledges that the second A37 term cannot be integrated to infinity after naively setting \(\alpha=0\). For a finite upper cutoff \(X\), its leading relative integrated size scales like

\[
\alpha\ln\!\left[1+(BX/\lambda)^2\right].
\]

Thus small \(\alpha\) alone is not a uniform bound over every simultaneous cutoff/parameter limit. However, using the actual Region-I scale \(X\) of order \(B\epsilon\), and the large-\(B\) scaling \(\lambda\sim B^{2/3}\epsilon\), this estimate is \(O(B^{-2/3}\ln B)\), which does tend to zero. It does not give a spurious \(\ln(1/\epsilon)\) objection to the usual matched limit. Region I must itself remain inside the sheet; an ordering such as \(B\epsilon\ll1\) is the natural inner-to-sheet restriction for the formal large-\(B\) extension.

A41 retains an asymptotic denominator \(1-\pi\lambda^3/(2B^2\epsilon^3)\), while dropping terms involving \(r\ln(B^2\epsilon/\lambda)\). Quantitative use arbitrarily close to that pole would require uniform remainder control; the displayed approximations do not make it an exact finite-\(B\) eigenvalue. This does not overturn the pole's order-of-magnitude scaling \(\lambda\sim B^{2/3}\epsilon\) in A44. With \(\delta\sim(\lambda\epsilon)^{1/2}\) and the crossover \(\delta\Delta'\sim1\), the implied wavenumber is \(k_{\max}a\sim\epsilon^{1/n}B^{1/(3n)}\). Multiplication by \(kb_a\) gives exactly A45,

\[
\gamma_{\max}\sim(b_a/a)\epsilon^{(n+1)/n}
B^{(2n+1)/(3n)}.
\]

The statement about convergence as \(B\to1\) is safe as a statement about these leading fastest-mode/crossover scalings. It should not be interpreted as pointwise identity of A21 and A23 for all \(\Delta'\). The ultrarelativistic sound-speed application has \(B\) of order unity; the large-\(B\) discussion is expressly a formal extension for the nonrelativistic analogy.

## Actual independent computation

`check_appendix_independently.py` was run under CPython 3.13.7 with mpmath 1.3.0 at 80 decimal digits. It uses exact standard-library fractions for 36 local-jet A1/A2-to-A3 controls, 36 independent chain-rule A30-to-A31 controls and 36 A8/A15-to-A7 controls. Six direct numerical A15 integrals reproduce A23; four independently evaluated A10/A12 pairs agree. Sixteen direct-versus-connection hypergeometric comparisons have maximum relative discrepancy \(4.22\times10^{-81}\). The coefficient, overlap and two fastest-mode exponent controls pass. The executable and JSON retain source-file hashes and explicit limits.

These checks are algebraic/special-function evidence. They are not a full A5 eigenmode computation, an independent physical validation of the fluid closure, a new kinetic simulation, a fit to either figure, or an identified hidden author-code behavior. The scratch receipt is `independent-appendix-checks.json`.
