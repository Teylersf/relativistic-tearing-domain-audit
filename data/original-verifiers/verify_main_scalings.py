"""Exact exponent controls for the source's declared phenomenological scalings.

No source numerical program, PIC field, particle distribution or ODE solution
is recovered. Numerical rows are logarithmic model examples, not astrophysical
measurements. All exponent identities use fractions.Fraction.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import platform
import sys

if sys.flags.optimize:
    raise RuntimeError("Run ordinary Python without -O; exact checks must remain enabled.")

HERE = Path(__file__).resolve().parent
CACHE = HERE.parent


def main():
    controls = []
    cases = []
    for n in (1, 2):
        # tau*gamma = (L/a)^(1/4)*(d/a)^(1+1/n).
        tearing_exponent = Q(n, 4 + 5*n)
        assert tearing_exponent * (Q(5, 4) + Q(1, n)) == Q(1, 4)
        # ach/d = sigma^(2/3)*R^(-1/3), R=L/d.
        ratio_R_exponent = -Q(1, 3) - tearing_exponent
        assert ratio_R_exponent == -Q(4 + 8*n, 12 + 15*n)
        sigma_tearing_first_exponent = -Q(3, 2)*ratio_R_exponent
        assert sigma_tearing_first_exponent == Q(2 + 4*n, 4 + 5*n)
        # Constant flux ba^2*gamma gives ba proportional to a^h.
        h = Q(2*n + 1, 3*n)
        assert 3*h - (2 + Q(1, n)) == 0
        spectrum_exponent = -(2*h + 1)
        assert spectrum_exponent == -Q(7*n + 2, 3*n)
        # The pre-tearing and tearing-mediated amplitudes match at at.
        assert (tearing_exponent - 1)/4 == -Q(1, 3) + h*tearing_exponent
        chi_a_exponent = 2*h - 2
        assert chi_a_exponent == Q(2*(1 - n), 3*n)
        chi_at_R_exponent = -Q(2, 3) + chi_a_exponent*tearing_exponent
        assert chi_at_R_exponent == -sigma_tearing_first_exponent
        assert chi_a_exponent == (0 if n == 1 else -Q(1, 3))
        controls.append({
            "profile_n": n,
            "at_over_d_power_of_R": str(tearing_exponent),
            "ach_over_at_power_of_R_at_fixed_sigma": str(ratio_R_exponent),
            "tearing_first_sigma_threshold_power": str(sigma_tearing_first_exponent),
            "tearing_range_ba_power_of_a": str(h),
            "one_dimensional_spectrum_power": str(spectrum_exponent),
            "charge_parameter_power_of_a_over_d": str(chi_a_exponent),
            "charge_parameter_at_d": "sigma_tilde * R^(-2/3)",
            "secondary_charge_scale": None if n == 1 else "a_star/d = sigma_tilde^3/R^2",
            "all_exponent_identities_pass": True,
        })
        for logR in (6, 30, 70, 140):
            for p in (Q(3, 5), Q(7, 10), Q(4, 5)):
                # sigma=R^p, represented by logarithms to avoid fake numerical
                # precision claims or overflow at formal asymptotic examples.
                log_sigma = p*logR
                log_at = tearing_exponent*logR
                log_ach = (-Q(1, 3) + 2*p/3)*logR
                log_chi_at = (p - sigma_tearing_first_exponent)*logR
                log_chi_d = (p - Q(2, 3))*logR
                tearing_first = p < sigma_tearing_first_exponent
                assert (log_ach < log_at) == tearing_first
                if not tearing_first:
                    regime = "charge_starvation_precedes_tearing_onset"
                    log_star = None
                elif n == 2 and p > Q(2, 3):
                    regime = "tearing_onset_then_charge_starvation_above_d"
                    log_star = (3*p - 2)*logR
                    assert Q(0) < log_star < log_at
                    # Substitution into the tearing-range charge parameter.
                    assert log_chi_d - log_star/3 == 0
                else:
                    regime = "tearing_first_no_charge_crossing_above_d_in_model"
                    log_star = (3*p - 2)*logR if n == 2 else None
                    assert log_chi_d < 0
                cases.append({
                    "profile_n": n, "log10_R": logR,
                    "sigma_power_p": str(p), "log10_sigma": str(log_sigma),
                    "log10_at_over_d": str(log_at),
                    "log10_ach_pretearing_over_d": str(log_ach),
                    "log10_charge_parameter_at_tearing_onset": str(log_chi_at),
                    "log10_charge_parameter_at_d_if_tearing_scaling_continued": str(log_chi_d),
                    "log10_secondary_charge_scale_over_d": str(log_star) if log_star is not None else None,
                    "regime_within_declared_scalings": regime,
                })

    # A parametrically separated omitted interval, not merely order-one
    # disagreement at a threshold where scaling coefficients are unknown.
    p = Q(7, 10)
    assert Q(2, 3) < p < Q(5, 7)
    assert p - Q(5, 7) < 0
    assert 3*p - 2 > 0
    assert 3*p - 2 - Q(1, 7) < 0
    window = {
        "profile_n": 2,
        "parameter_family": "R->infinity, sigma_tilde=R^p, 2/3<p<5/7",
        "selected_p": str(p),
        "sigma_over_tearing_threshold_power": str(p - Q(5, 7)),
        "a_star_over_d_power": str(3*p - 2),
        "a_star_over_at_power": str(3*p - 2 - Q(1, 7)),
        "tearing_first_and_secondary_charge_crossing_parametrically_compatible": True,
    }
    sources = []
    for name in ("supplied.pdf", "journal-browser-math-tex.json"):
        b = (CACHE/name).read_bytes()
        sources.append({"filename": name, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()})
    out = {
        "schema_version": 1, "all_checks_passed": True,
        "scope": "Declared fixed-parameter phenomenological main-equation scaling identities; no new fluid/PIC/particle evolution or astrophysical measurement.",
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python_version": platform.python_version(), "sources": sources,
        "positive_scaling_controls": controls, "logarithmic_model_examples": cases,
        "conditional_secondary_starvation_window": window,
        "source_locators": {
            "tearing_onset": "Eqs7,9-13 pp3",
            "charge_parameter_and_scale": "Eqs14-20 pp3-4",
            "tearing_range_flux_and_secondary_scale": "Eqs21-25 p4",
            "source_qualification": "p4 paragraph after Eq25 explicitly expects a_star<d in astrophysical systems and conditions its conclusion on that expectation",
            "broader_conclusion": "Abstractp1 and conclusionp5 Eqs27-32",
        },
        "limits": [
            "Main tearing-onset inequality is not refuted; the secondary issue concerns continuation of the localized-profile cascade below onset.",
            "All results are conditional on adopted dynamic-alignment, constant-flux, profile-index and fixed-inertial-scale assumptions.",
            "No actual astrophysical R or sigma has been inferred; large logarithmic examples are formal controls, not physical parameter estimates.",
            "The source explicitly states the a_star<d expectation on p4; that qualification must not be omitted when describing the finding.",
            "Changing density, heating, kinetic dispersion, damping, radiation or cascade structure can alter the evolution; none is newly solved here.",
            "No new spectrum below secondary charge starvation, reconnection rate or PIC outcome is supplied.",
        ],
    }
    pth = HERE/"main-scaling-checks.json"
    pth.write_text(json.dumps(out,indent=2,allow_nan=False)+"\n",encoding="utf-8",newline="\n")
    print(json.dumps({"all_checks_passed": True, "profiles": 2, "model_examples": len(cases),
                      "receipt_sha256": hashlib.sha256(pth.read_bytes()).hexdigest()}))


if __name__ == "__main__":
    main()
