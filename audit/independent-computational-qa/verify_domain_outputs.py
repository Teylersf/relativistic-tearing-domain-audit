"""Read-only exact checks of a prepared domain package, without producer import."""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import csv
import hashlib
import itertools
import json
import platform
import struct
import sys


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(path):
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def independently_derive(n, r, s):
    # Solve (r-x)/4 = (1+1/n)x for initial tearing/cascade equality.
    tearing_power = 1 + Q(1, n)
    xt = r / (4*tearing_power+1)
    b_at = (xt-r)/4
    # Constant flux: three times the amplitude slope minus2 minus1/n=0.
    h = Q(2+Q(1, n), 3)
    offset = b_at-h*xt
    # Current demand is log C = s +2 log(b/b0) -2x.
    intercept, slope = s+2*offset, 2*h-2
    xch = (2*s-r)/3  # Root of the initial aligned-cascade demand.
    star = -intercept/slope if slope else None
    c_at, c_d = intercept+slope*xt, intercept
    if xch > xt:
        regime = "initial_charge_crossing_before_tearing_onset"
        valid = False
    elif xch == xt:
        regime = "coincident_initial_thresholds_no_scale_separation"
        valid = False
    elif n == 1:
        assert slope == 0
        regime = "Harris_tearing_first_no_post_tearing_crossing"
        valid = True
    else:
        valid = True
        assert star is not None
        tail = "below_d" if star < 0 else "at_d" if star == 0 else "above_d"
        regime = "localized_tearing_first_secondary_crossing_"+tail
    return {
        "n": n, "log10_R": r, "log10_sigma_tilde": s,
        "sigma_power_of_R": s/r, "log10_x_t": xt,
        "log10_x_ch_unmodified": xch, "log10_C_at_onset": c_at,
        "log10_C_at_d_if_continued": c_d,
        "log10_x_star_if_localized": star,
        "post_tearing_branch_initially_below_current_threshold": valid,
        "regime_under_unity_prefactors": regime,
    }, {"amplitude_slope": h, "current_slope": slope}


def match_row(actual, expected):
    for key, value in expected.items():
        cell = actual[key]
        if value is None:
            assert cell == "", (key, cell)
        elif isinstance(value, bool):
            assert cell == str(value), (key, cell)
        elif isinstance(value, (Q, int)):
            assert Q(cell) == value, (key, cell, str(value))
        else:
            assert cell == value, (key, cell)


def main():
    if sys.flags.optimize:
        raise RuntimeError("Use ordinary Python without -O; exact checks must remain enabled.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    targets = [root/"reproduction/run_audit.py", *sorted((root/"data").glob("*")),
               *sorted((root/"figures").glob("*.png"))]
    targets = [p for p in targets if p.is_file()]
    before = {p.relative_to(root).as_posix(): digest(p) for p in targets}
    result = json.loads((root/"data/producer-results.json").read_text(encoding="utf-8"))
    assert result["producer_sha256"] == before["reproduction/run_audit.py"]
    all_rows = read_csv(root/"data/finite-domain-cases.csv")
    assert len(all_rows) == 144
    expected_keys = set(itertools.product([1, 2], [3, 6, 12, 30, 42, 84, 126, 210],
                                         map(Q, ["-1/10", "0", "1/3", "3/5", "2/3",
                                                 "29/42", "5/7", "4/5", "1"])))
    actual_keys, counts = set(), {}
    for row in all_rows:
        n, r, s = int(row["n"]), Q(row["log10_R"]), Q(row["log10_sigma_tilde"])
        actual_keys.add((n, r, s/r))
        expected, unused = independently_derive(n, r, s)
        match_row(row, expected)
        regime = expected["regime_under_unity_prefactors"]
        counts[regime] = counts.get(regime, 0)+1
    assert actual_keys == expected_keys and len(actual_keys) == 144
    assert counts == result["finite_log_grid"]["regime_counts"]
    fixed = [row for row in all_rows if row["n"] == "2"
             and Q(row["log10_sigma_tilde"]) == 0]
    assert len(fixed) == 8
    fixed_roots = [Q(row["log10_x_star_if_localized"]) for row in fixed]
    assert all(x == -2*Q(row["log10_R"]) for x, row in zip(fixed_roots, fixed))
    assert all(a > b for a, b in zip(fixed_roots, fixed_roots[1:]))
    assert result["fixed_magnetization_limit"]["exact_grid_controls_at_sigma_equal_one"] == 8
    assert not result["fixed_magnetization_limit"]["source_fixed_parameter_expectation_contradicted"]
    equalities = read_csv(root/"data/transition-cases.csv")
    expected_equalities = [r for r in all_rows if Q(r["log10_C_at_onset"]) == 0
                           or (r["n"] == "2" and Q(r["log10_C_at_d_if_continued"]) == 0)]
    assert equalities == expected_equalities and len(equalities) == 24
    witnesses = read_csv(root/"data/formal-witnesses.csv")
    assert len(witnesses) == 3
    for m, row in enumerate(witnesses, 1):
        expected, unused = independently_derive(2, Q(42*m), Q(29*m))
        match_row(row, expected)
        assert Q(row["log10_x_star_over_x_t"]) == -3*m
        assert Q(row["log10_sigma_over_R_two_thirds"]) == m
        assert Q(row["log10_R_five_sevenths_over_sigma"]) == m
    trajectories = read_csv(root/"data/trajectory-cases.csv")
    assert len(trajectories) == 3
    for row, (n, r, s) in zip(trajectories, [(2, 42, 26), (2, 42, 29), (1, 42, 26)]):
        expected, unused = independently_derive(n, Q(r), Q(s))
        match_row(row, expected)
    profiles = read_csv(root/"data/profile-exponents.csv")
    assert len(profiles) == 2
    for row, n in zip(profiles, [1, 2]):
        r = Q(1)
        expected, derived = independently_derive(n, r, Q(0))
        match_row(row, {"n": n, "onset_R_exponent": expected["log10_x_t"],
                       "post_amplitude_x_exponent": derived["amplitude_slope"],
                       "one_dimensional_spectrum_exponent": -(2*derived["amplitude_slope"]+1),
                       "post_charge_x_exponent": derived["current_slope"],
                       "onset_sigma_threshold_R_exponent": -expected["log10_C_at_onset"]})
    image_sizes = {}
    for name in ["phase-domains.png", "current-demand-trajectories.png"]:
        raw = (root/"figures"/name).read_bytes()
        assert raw[:8] == b"\x89PNG\r\n\x1a\n" and raw[12:16] == b"IHDR"
        image_sizes[name] = list(struct.unpack(">II", raw[16:24]))
        assert min(image_sizes[name]) >= 1000
    for row in result["artifacts"]:
        p = root/row["path"]
        assert p.stat().st_size == row["bytes"] and digest(p) == row["sha256"]
    assert result["source_caveat_credited"] and result["unity_prefactors_declared"]
    assert result["new_PIC_MHD_or_full_inner_ODE_runs"] == 0
    assert before == {p.relative_to(root).as_posix(): digest(p) for p in targets}
    receipt = {
        "schema_version": 1, "status": "pass",
        "environment": {"python": platform.python_version(), "standard_library_only": True},
        "verifier_SHA256": digest(Path(__file__)),
        "producer_imported_or_executed": False,
        "exact_finite_cases_independently_derived": 144,
        "equality_cases": 24, "formal_witnesses": 3, "trajectory_cases": 3,
        "fixed_magnetization_cases": 8,
        "profile_cases": 2, "regime_counts": counts, "PNG_dimensions": image_sizes,
        "producer_artifact_manifest_matches": True, "all_reviewed_input_bytes_unchanged": True,
        "bound_SHA256": before,
        "limits": "Exact algebra and file-integrity controls only. Visual and source-scope assessment are recorded separately; no physical calibration or post-threshold prediction is certified."
    }
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"status": "pass", "finite_cases": 144,
                      "receipt_SHA256": digest(args.receipt)}))


if __name__ == "__main__":
    main()
