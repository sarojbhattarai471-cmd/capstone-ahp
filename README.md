# Decentralized Storage Prioritisation — AHP · TOPSIS · Sensitivity Analysis

PRJ701 Capstone Project — a decision-support tool for prioritising decentralized-storage
techniques in energy blockchain systems, using the Analytic Hierarchy Process (AHP) for
criteria weighting, TOPSIS for ranking fifteen storage techniques, and Sensitivity Analysis
to test ranking stability. Full results export to Excel.

**Live demo:** https://capstone-ahp.onrender.com
*(free tier — spins down after 15 minutes idle, first load after that takes ~1 minute to wake up)*

**Group:** Saroj · Niraj · Hemant — KIHE

## Run it locally

```bash
git clone https://github.com/sarojbhattarai471-cmd/capstone-ahp.git
cd capstone-ahp
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./run.sh
```

Then open http://localhost:8501 in your browser.

## What it does

- Explains Saaty's 1–9 pairwise comparison scale
- Three switchable expert profiles, each with 10 pairwise sliders (5 criteria → C(5,2) = 10 comparisons)
- Computes AHP criterion weights and consistency ratio (CR) live
- Aggregates saved experts into final weights, then ranks 15 storage techniques with TOPSIS
- Runs a full sensitivity analysis (±10%/±20% per criterion) to check ranking stability
- Exports every stage — pairwise matrices, AHP weights, TOPSIS ranking, sensitivity results,
  and the decision matrix — to a single downloadable Excel workbook

## Project structure

```
app.py              # Streamlit UI and page flow
core/
  data.py           # Criteria, techniques, expert defaults
  ahp.py            # AHP pairwise-comparison math
  topsis.py         # TOPSIS ranking and sensitivity analysis
  excel_export.py   # Excel workbook generation
ui/
  styles.py         # Page CSS and hero/header markup
requirements.txt    # streamlit, pandas, numpy, openpyxl
run.sh              # Activates venv and launches the app
```

## Research basis

He et al. (2024), Table 1.
