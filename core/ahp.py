"""Analytic Hierarchy Process (AHP) computations."""

import numpy as np

from core.data import CENTER, N, RI_TABLE


def slider_to_aij(pos):
    if pos == CENTER:
        return 1.0
    if pos < CENTER:
        return float((CENTER - pos) + 1)
    return 1.0 / ((pos - CENTER) + 1)


def judgement_sentence(pos, left, right):
    if pos == CENTER:
        return f"**{left}** and **{right}** are equally important."
    if pos < CENTER:
        strength = (CENTER - pos) + 1
        return f"**{left}** is preferred over **{right}** — strength {strength}."
    strength = (pos - CENTER) + 1
    return f"**{right}** is preferred over **{left}** — strength {strength}."


def build_matrix(positions):
    matrix = np.ones((N, N))
    for (i, j), pos in positions.items():
        value = slider_to_aij(pos)
        matrix[i, j] = value
        matrix[j, i] = 1 / value
    return matrix


def compute_ahp(matrix):
    normalised = matrix / matrix.sum(axis=0)
    weights = normalised.mean(axis=1)
    weighted_sum = matrix @ weights
    lambda_max = np.mean(weighted_sum / weights)
    ci = (lambda_max - N) / (N - 1)
    cr = ci / RI_TABLE[N]
    return weights, lambda_max, ci, cr
