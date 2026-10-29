"""Independent exact-exponent controls for a conditional source-domain map.

Standard library only; no source-PDF parsing, network or plasma evolution.
All physical identifications are assumptions to be assessed in the prose note.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import math
import platform
import sys

if sys.flags.optimize:
    raise RuntimeError("Run without -O; exact verification guards must remain enabled.")


def record(p):
    return {
        "p": str(p),
        "a_star_over_d_exponent": str(3*p-2),
        "a_star_over_a_t_exponent": str(3*p-F(15, 7)),
        "unmodified_a_ch_over_a_t_exponent": str(F(2, 3)*p-F(10, 21)),
        "current_proxy_at_a_t_exponent": str(p-F(5, 7)),
        "normalized_fluctuation_at_a_star_exponent": str(F(5, 2)*p-2),
    }


def main():
    lower, upper = F(2, 3), F(5, 7)
    midpoint = (lower+upper)/2
    assert midpoint == F(29, 42) and upper-lower == F(1, 21)
    inside = []
    for j in range(1, 21):
        p = lower+(upper-lower)*F(j, 21)
        assert 3*p-2 > 0 and 3*p-F(15, 7) < 0
        assert F(2, 3)*p-F(10, 21) < 0
        assert p-F(5, 7) < 0 and F(5, 2)*p-2 < 0
        # chi(x)=sigma_tilde R^(-2/3) x^(-1/3); x*=R^(3p-2).
        assert p-F(2, 3)-F(1, 3)*(3*p-2) == 0
        # A still stronger guide can be chosen with deltaB0/B0=R^(-q).
        q = F(1, 100)
        assert p+2*q > p and F(5, 2)*p-2-q < 0
        inside.append(record(p))
    boundaries = [record(p) for p in [F(3, 5), lower, upper, F(3, 4)]]
    assert 3*F(3, 5)-2 < 0
    assert 3*lower-2 == 0
    assert 3*upper-F(15, 7) == 0
    assert F(3, 4)-upper > 0
    assert 3*midpoint-2 == F(1, 14)
    assert F(1, 7)-(3*midpoint-2) == F(1, 14)
    finite = []
    for logR in [6, 9, 12, 18, 21, 42, 84, 126]:
        finite.append({"log10_R": logR,
                       "window_upper_over_lower": 10**(logR/21),
                       "largest_equal_magnetization_margins": 10**(logR/42),
                       "midpoint_a_star_over_d": 10**(logR/14),
                       "midpoint_a_t_over_a_star": 10**(logR/14),
                       "midpoint_original_a_ch_over_a_t": 10**(-logR/63)})
    fit = []
    for n in (1, 2):
        for x in (10., 1000., 1e6):
            k_a = x**(-1/n)
            ell_a = x**(1+1/n)
            error = abs(k_a*ell_a/x-1)
            assert error < 1e-14
            fit.append({"n": n, "a_over_d": x,
                        "kmax_a": k_a, "eddy_length_over_a": ell_a,
                        "kmax_eddy_length": k_a*ell_a,
                        "relative_identity_error": error})
    # Source n=1 post-onset b_a/b0=R^(-1/3)*x gives constant proxy.
    R, sig = 1e12, 1e6
    harris = [sig*(R**(-1/3)*x)**2/x**2 for x in [1., 10., 1e3]]
    assert max(harris)-min(harris) < 1e-14
    result = {
        "schema_version": 1, "status": "pass",
        "environment": {"python": platform.python_version(), "standard_library_only": True},
        "program_SHA256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Exact exponents and scalar consistency controls, not an astrophysical parameter inference, nonlinear plasma solution or kinetic validation.",
        "assumptions": ["R=L_perp/d_rel>1; fixed density and enthalpy.",
                        "n=2 source post-onset amplitude scaling and current proxy retained only up to prospective charge-starvation onset.",
                        "Order-one prefactors omitted, as in the source scaling estimates.",
                        "Mode-fit control assumes the stated tearing-time/nonlinear-time balance and the usual velocity-amplitude eddy length."],
        "inside_window_exact_controls": inside,
        "outside_and_boundary_controls": boundaries,
        "finite_scale_separation_controls": finite,
        "mode_fit_controls": fit,
        "Harris_constant_current_proxy_control": harris,
        "strong_margin_condition": "Both sigma_tilde/R^(2/3)>K and R^(5/7)/sigma_tilde>K require R>K^42.",
        "conditional_exact_current_prefactor": "If n=n0 is each-species density, physical Ampere current divided by2n0ec has squared ratio equal to one-half the source proxy. This changes order-one thresholds, not powers. Density/normalization conventions must be fixed before treating it as an exact correction.",
        "limits": ["No claim that the formal asymptotic family is realized in a pulsar wind nebula or any other measured source.",
                   "No spectrum, heating or field evolution is predicted after the nonrelativistic bulk-current description fails.",
                   "No hidden equality relating guide magnetization, fluctuation amplitude, density, temperature and system size was supplied by the source or inferred from this program."]
    }
    target = Path(__file__).with_name("parameter-window-controls.json")
    target.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({"status": "pass", "inside_exact_cases": len(inside),
                      "boundaries_and_outside": len(boundaries), "finite_R_cases": len(finite),
                      "mode_fit_cases": len(fit), "program_SHA256": result["program_SHA256"],
                      "JSON_SHA256": hashlib.sha256(target.read_bytes()).hexdigest()}))


if __name__ == "__main__":
    main()
