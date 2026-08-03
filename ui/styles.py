"""CSS and static header/hero markup for the Streamlit page."""

CUSTOM_CSS = """
<style>
:root {
    --navy: #16302A;
    --blue: #22463C;
    --royal: #2E5C4E;
    --gold: #C1703B;
    --paper: #F6F7F3;
    --ink: #1B211D;
    --muted: #5C6B62;
    --line: #DEE5DD;
    --white: #FFFFFF;
}

.stApp {
    background: var(--paper);
    color: var(--ink);
}

.block-container {
    max-width: 1240px;
    padding-top: 1.2rem;
    padding-bottom: 4rem;
}

#MainMenu, footer {
    visibility: hidden;
}

.uni-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 1rem;
    background: var(--navy);
    color: white;
    border-radius: 18px;
    padding: 1rem 1.25rem;
    box-shadow: 0 12px 32px rgba(22, 48, 42, 0.18);
    margin-bottom: 1rem;
}

.uni-brand {
    display: flex;
    align-items: center;
    gap: 0.9rem;
}

.uni-mark {
    display: grid;
    place-items: center;
    width: 46px;
    height: 46px;
    border: 2px solid rgba(255,255,255,0.85);
    border-radius: 50%;
    font-size: 1.25rem;
    font-weight: 800;
    color: var(--gold);
}

.uni-title {
    font-size: 1.08rem;
    font-weight: 800;
    letter-spacing: 0.01em;
}

.uni-subtitle {
    color: rgba(255,255,255,0.72);
    font-size: 0.82rem;
    margin-top: 0.1rem;
}

.project-chip {
    border: 1px solid rgba(255,255,255,0.22);
    background: rgba(255,255,255,0.08);
    padding: 0.52rem 0.8rem;
    border-radius: 999px;
    color: white;
    font-size: 0.78rem;
    font-weight: 700;
    white-space: nowrap;
}

.hero {
    position: relative;
    overflow: hidden;
    border-radius: 24px;
    padding: 2.4rem;
    background:
        radial-gradient(circle at 85% 15%, rgba(193,112,59,0.26), transparent 22%),
        linear-gradient(135deg, #16302A 0%, #22463C 58%, #2E5C4E 100%);
    color: white;
    box-shadow: 0 20px 55px rgba(46, 92, 78, 0.22);
    margin-bottom: 1.2rem;
}

.hero-kicker {
    color: #E7B182;
    text-transform: uppercase;
    letter-spacing: 0.13em;
    font-size: 0.76rem;
    font-weight: 800;
    margin-bottom: 0.65rem;
}

.hero h1 {
    color: white !important;
    font-size: clamp(2rem, 4vw, 3.25rem);
    max-width: 900px;
    line-height: 1.08;
    letter-spacing: -0.035em;
    margin: 0 0 0.8rem 0;
}

.hero p {
    color: rgba(255,255,255,0.84);
    max-width: 840px;
    font-size: 1rem;
    line-height: 1.72;
    margin: 0;
}

.hero-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 1.6rem;
    margin-top: 1.4rem;
    padding-top: 1.2rem;
    border-top: 1px solid rgba(255,255,255,0.16);
}

.hero-meta-item {
    min-width: 170px;
}

.hero-meta-label {
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-size: 0.68rem;
    font-weight: 700;
    color: rgba(255,255,255,0.55);
    margin-bottom: 0.2rem;
}

.hero-meta-value {
    color: white;
    font-size: 0.92rem;
    font-weight: 700;
}

.overview-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 0.85rem;
    margin: 1rem 0 1.3rem 0;
}

.overview-card {
    background: white;
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 1rem;
    box-shadow: 0 8px 24px rgba(27,33,29,0.055);
}

.overview-number {
    color: var(--royal);
    font-size: 1.4rem;
    font-weight: 850;
}

.overview-label {
    color: var(--muted);
    font-size: 0.82rem;
    margin-top: 0.2rem;
}

.section-card {
    background: white;
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 1.25rem 1.35rem;
    box-shadow: 0 8px 26px rgba(27,33,29,0.055);
    margin-bottom: 1rem;
}

.section-card h2, .section-card h3 {
    margin: 0 0 0.35rem 0;
    color: var(--navy);
}

.section-card p {
    color: var(--muted);
    margin: 0;
    line-height: 1.65;
}

.research-note {
    border-left: 4px solid var(--gold);
    background: #FBF1E8;
    color: #5A3420;
    border-radius: 0 14px 14px 0;
    padding: 0.9rem 1rem;
    margin-bottom: 1rem;
    font-size: 0.9rem;
}

div[data-testid="stMetric"] {
    background: white;
    border: 1px solid var(--line);
    padding: 1rem;
    border-radius: 16px;
    box-shadow: 0 7px 20px rgba(27,33,29,0.05);
}

div[data-testid="stRadio"] > div {
    background: white;
    border: 1px solid var(--line);
    padding: 0.75rem 0.9rem;
    border-radius: 14px;
}

.stButton > button,
.stDownloadButton > button {
    border-radius: 11px;
    min-height: 2.8rem;
    font-weight: 760;
    border: 1px solid transparent;
}

.stButton > button[kind="primary"],
.stDownloadButton > button[kind="primary"] {
    background: linear-gradient(135deg, var(--blue), var(--royal));
    color: white;
    box-shadow: 0 8px 20px rgba(46,92,78,0.22);
}

[data-testid="stDataFrame"] {
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid var(--line);
    background: white;
}

[data-testid="stTabs"] button {
    font-weight: 750;
}

h1, h2, h3 {
    color: var(--navy);
    letter-spacing: -0.02em;
}

@media (max-width: 800px) {
    .overview-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }
    .project-chip {
        display: none;
    }
    .hero {
        padding: 1.5rem;
    }
}
</style>
"""

HEADER_HERO_HTML = """
<div class="uni-header">
    <div class="uni-brand">
        <div class="uni-mark">DS</div>
        <div>
            <div class="uni-title">Decentralized Storage Research Portal</div>
            <div class="uni-subtitle">PRJ701 Capstone Research Project</div>
        </div>
    </div>
    <div class="project-chip">AHP · TOPSIS · Sensitivity Analysis</div>
</div>

<div class="hero">
    <div class="hero-kicker">University research decision-support system</div>
    <h1>Prioritisation Framework for Decentralized Storage in Energy Blockchain</h1>
    <p>
        This application evaluates five research criteria, derives their relative importance
        through the Analytic Hierarchy Process, ranks fifteen decentralized-storage techniques
        using TOPSIS, tests ranking stability through Sensitivity Analysis, and exports the
        complete results to Excel.
    </p>
    <div class="hero-meta">
        <div class="hero-meta-item">
            <div class="hero-meta-label">Study</div>
            <div class="hero-meta-value">Decentralized Storage Prioritisation Framework</div>
        </div>
        <div class="hero-meta-item">
            <div class="hero-meta-label">Method</div>
            <div class="hero-meta-value">AHP pairwise comparison — Saaty 1–9 scale</div>
        </div>
        <div class="hero-meta-item">
            <div class="hero-meta-label">Comparisons</div>
            <div class="hero-meta-value">10 pairs across 5 criteria</div>
        </div>
        <div class="hero-meta-item">
            <div class="hero-meta-label">Group</div>
            <div class="hero-meta-value">Saroj · Niraj · Hemant — KIHE</div>
        </div>
    </div>
</div>

<div class="overview-grid">
    <div class="overview-card">
        <div class="overview-number">5</div>
        <div class="overview-label">Assessment criteria</div>
    </div>
    <div class="overview-card">
        <div class="overview-number">15</div>
        <div class="overview-label">Storage techniques</div>
    </div>
    <div class="overview-card">
        <div class="overview-number">3</div>
        <div class="overview-label">Expert profiles</div>
    </div>
    <div class="overview-card">
        <div class="overview-number">4</div>
        <div class="overview-label">Analysis stages</div>
    </div>
</div>

<div class="research-note">
    Research basis: He et al. (2024), Table 1. The application is intended as a structured
    decision-support prototype for the PRJ701 capstone project.
</div>
"""

FOOTER_HTML = """
<div style="text-align:center;color:#6B7787;font-size:0.8rem;padding-top:2rem;">
    PRJ701 Capstone Research Project · Decentralized Storage Prioritisation Framework
</div>
"""
