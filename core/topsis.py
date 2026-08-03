"""TOPSIS ranking and sensitivity analysis."""

import numpy as np
import pandas as pd

from core.data import CRITERIA, TECHNIQUES


def run_topsis(weights):
    decision = np.array([item[2] for item in TECHNIQUES], dtype=float)
    denominator = np.sqrt((decision ** 2).sum(axis=0))
    normalised = decision / denominator
    weighted = normalised * weights
    ideal_best = weighted.max(axis=0)
    ideal_worst = weighted.min(axis=0)
    s_plus = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    s_minus = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))
    closeness = s_minus / (s_plus + s_minus)
    ranks = pd.Series(closeness).rank(method="min", ascending=False).astype(int).to_numpy()

    return pd.DataFrame({
        "Alternative": [x[0] for x in TECHNIQUES],
        "Technique": [x[1] for x in TECHNIQUES],
        "S+": s_plus,
        "S-": s_minus,
        "Closeness": closeness,
        "Rank": ranks,
    }).sort_values(["Rank", "Alternative"])


def run_sensitivity(base_weights, base_topsis):
    results = []
    base_rank = dict(zip(base_topsis["Alternative"], base_topsis["Rank"]))

    scenarios = [("Original", None, 0)]
    for idx, criterion in enumerate(CRITERIA):
        scenarios.append((f"{criterion['id']} +10%", idx, 0.10))
        scenarios.append((f"{criterion['id']} -10%", idx, -0.10))
        scenarios.append((f"{criterion['id']} +20%", idx, 0.20))
        scenarios.append((f"{criterion['id']} -20%", idx, -0.20))

    for scenario_name, index, change in scenarios:
        weights = base_weights.copy()
        if index is not None:
            weights[index] = max(0.0001, weights[index] * (1 + change))
            weights = weights / weights.sum()

        scenario_topsis = run_topsis(weights)
        scenario_rank = dict(zip(scenario_topsis["Alternative"], scenario_topsis["Rank"]))
        changed = any(scenario_rank[a] != base_rank[a] for a in base_rank)

        row = {"Scenario": scenario_name}
        for i, criterion in enumerate(CRITERIA):
            row[criterion["id"]] = weights[i]
        row["Ranking Changed?"] = "Yes" if changed else "No"
        row["Top Alternative(s)"] = ", ".join(
            scenario_topsis.loc[scenario_topsis["Rank"] == 1, "Alternative"].tolist()
        )
        results.append(row)

    return pd.DataFrame(results)
