"""
Static project data: criteria, techniques, experts, and scale definitions
for the Decentralized Storage AHP/TOPSIS capstone project.
"""

CRITERIA = [
    {"id": "C1", "name": "Single Point Failure"},
    {"id": "C2", "name": "Malicious Tampering"},
    {"id": "C3", "name": "Storage Efficiency"},
    {"id": "C4", "name": "Enhanced Transparency"},
    {"id": "C5", "name": "Enhanced Trust"},
]

TECHNIQUES = [
    ("A1", "Wang et al. [15] — Consortium blockchain", [9, 9, 1, 1, 1]),
    ("A2", "Loka et al. [19] — Smart contracts", [9, 9, 1, 1, 1]),
    ("A3", "Wu et al. [20] — Consortium blockchain", [9, 9, 1, 1, 1]),
    ("A4", "Zakaret et al. [21] — Security components integration", [1, 9, 1, 1, 1]),
    ("A5", "Zhang et al. [22] — Master–slave architecture", [9, 9, 1, 1, 1]),
    ("A6", "Li et al. [23] — Consensus mechanism", [9, 9, 1, 1, 1]),
    ("A7", "Chen and Zhang [24] — Consortium blockchain", [9, 9, 1, 1, 1]),
    ("A8", "Cai et al. [25] — Data compression and alignment", [1, 1, 9, 1, 1]),
    ("A9", "Miyamae et al. [26] — Zero knowledge proof", [1, 1, 9, 1, 1]),
    ("A10", "Chen et al. [27] — Parameter synchronization", [1, 1, 9, 1, 1]),
    ("A11", "Wu et al. [28] — Hybrid public-private blockchain", [1, 1, 9, 1, 1]),
    ("A12", "Zhao et al. [29] — Dual-layer transaction framework", [1, 1, 1, 9, 9]),
    ("A13", "Singh et al. [30] — Smart contracts", [1, 1, 1, 9, 9]),
    ("A14", "Jiang et al. [31] — Trust hierarchies", [1, 1, 1, 9, 9]),
    ("A15", "Skowroński [32] — System integration", [1, 1, 1, 9, 9]),
]

EXPERTS = ["Expert 1", "Expert 2", "Expert 3"]
N = len(CRITERIA)
PAIRS = [(i, j) for i in range(N) for j in range(i + 1, N)]
CENTER = 8

SLIDER_LABELS = [
    "9 ◀ left extreme", "8", "7", "6", "5", "4", "3", "2",
    "1 = Equal",
    "2", "3", "4", "5", "6", "7", "8", "9 ▶ right extreme",
]

# Scenario-based Generative-AI defaults
EXPERT_DEFAULTS = {
    "Expert 1": {
        (0, 1): 8, (0, 2): 7, (0, 3): 6, (0, 4): 6,
        (1, 2): 7, (1, 3): 5, (1, 4): 5,
        (2, 3): 7, (2, 4): 7, (3, 4): 8,
    },
    "Expert 2": {
        (0, 1): 8, (0, 2): 10, (0, 3): 7, (0, 4): 8,
        (1, 2): 9, (1, 3): 7, (1, 4): 8,
        (2, 3): 11, (2, 4): 10, (3, 4): 9,
    },
    "Expert 3": {
        (0, 1): 9, (0, 2): 9, (0, 3): 10, (0, 4): 10,
        (1, 2): 8, (1, 3): 9, (1, 4): 9,
        (2, 3): 9, (2, 4): 9, (3, 4): 8,
    },
}

RI_TABLE = {1: 0, 2: 0, 3: 0.58, 4: 0.90, 5: 1.12}
