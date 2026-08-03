"""
PRJ701 Capstone Project
Decentralized Storage Prioritisation using AHP, TOPSIS and Sensitivity Analysis
"""

import pandas as pd
import streamlit as st

from core.ahp import build_matrix, compute_ahp, judgement_sentence
from core.data import CRITERIA, EXPERT_DEFAULTS, EXPERTS, PAIRS, SLIDER_LABELS
from core.excel_export import create_results_workbook
from ui.styles import CUSTOM_CSS, FOOTER_HTML, HEADER_HERO_HTML

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(
    page_title="Decentralized Storage Prioritisation",
    page_icon="🎓",
    layout="wide",
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
st.markdown(HEADER_HERO_HTML, unsafe_allow_html=True)

# -----------------------------
# Session state
# -----------------------------
if "positions" not in st.session_state:
    st.session_state.positions = {
        expert: EXPERT_DEFAULTS[expert].copy()
        for expert in EXPERTS
    }

if "saved_experts" not in st.session_state:
    st.session_state.saved_experts = {}

# -----------------------------
# Tabs
# -----------------------------
tab_home, tab_assessment, tab_results = st.tabs(
    ["Project Overview", "Expert Assessment", "Results & Download"]
)

with tab_home:
    st.markdown(
        """
        <div class="section-card">
            <h2>Research objective</h2>
            <p>
                The purpose of this application is to provide a transparent and repeatable method
                for prioritising decentralized-storage techniques when several competing criteria
                must be considered at the same time.
            </p>
        </div>

        <div class="section-card">
            <h3>Evaluation process</h3>
            <p>
                1. Complete pairwise comparisons for the five criteria.<br>
                2. Calculate AHP criterion weights and verify consistency.<br>
                3. Rank the fifteen techniques using TOPSIS.<br>
                4. Test ranking stability using Sensitivity Analysis.<br>
                5. Download the complete workbook for research submission.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    criteria_df = pd.DataFrame({
        "ID": [c["id"] for c in CRITERIA],
        "Assessment criterion": [c["name"] for c in CRITERIA],
        "Purpose": [
            "Reduce dependence on a single trusted storage centre",
            "Prevent unauthorised or malicious modification of stored data",
            "Reduce storage size and processing overhead",
            "Improve visibility and auditability of stored data",
            "Build stakeholder confidence in data integrity",
        ],
    })
    st.subheader("Assessment criteria")
    st.dataframe(criteria_df, hide_index=True, use_container_width=True)

with tab_assessment:
    st.markdown(
        """
        <div class="section-card">
            <h2>Expert pairwise assessment</h2>
            <p>
                Select an expert profile and compare each pair of criteria using Saaty's 1–9 scale.
                The AHP weights and consistency ratio update automatically.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    expert = st.radio(
        "Choose an expert profile",
        EXPERTS,
        horizontal=True,
        help="Each profile stores its own set of pairwise comparisons.",
    )

    st.subheader(f"Pairwise comparisons — {expert}")

    for idx, (i, j) in enumerate(PAIRS):
        left = CRITERIA[i]
        right = CRITERIA[j]
        key = f"{expert}_{left['id']}_{right['id']}"

        st.markdown(
            f"**Question {idx + 1} of {len(PAIRS)}:** "
            f"{left['name']} ({left['id']}) vs {right['name']} ({right['id']})"
        )

        position = st.select_slider(
            " ",
            options=list(range(17)),
            value=st.session_state.positions[expert][(i, j)],
            format_func=lambda p: SLIDER_LABELS[p],
            key=key,
            label_visibility="collapsed",
        )

        st.session_state.positions[expert][(i, j)] = position
        st.caption(judgement_sentence(position, left["name"], right["name"]))
        st.divider()

    positions = st.session_state.positions[expert]
    matrix = build_matrix(positions)
    weights, lambda_max, ci, cr = compute_ahp(matrix)

    st.markdown(
        """
        <div class="section-card">
            <h2>AHP result</h2>
            <p>
                A consistency ratio below 10% indicates that the pairwise judgements are acceptably consistent.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Consistency Ratio", f"{cr:.2%}")
    col2.metric("Consistency status", "Acceptable" if cr < 0.10 else "Review required")
    col3.metric("Criteria assessed", len(CRITERIA))

    weights_df = pd.DataFrame({
        "Criterion": [c["name"] for c in CRITERIA],
        "ID": [c["id"] for c in CRITERIA],
        "Weight": weights,
    })

    chart_col, table_col = st.columns([1, 1.15])
    with chart_col:
        st.subheader("Criterion weight chart")
        chart_data = weights_df.set_index("ID")[["Weight"]]
        st.bar_chart(chart_data, use_container_width=True)
    with table_col:
        st.subheader("Criterion weight table")
        st.dataframe(
            weights_df.style.format({"Weight": "{:.2%}"}),
            hide_index=True,
            use_container_width=True,
        )

    if st.button(f"Save {expert}'s AHP responses", type="primary"):
        st.session_state.saved_experts[expert] = {
            "positions": positions.copy(),
            "matrix": matrix.copy(),
            "weights": weights.copy(),
            "cr": cr,
        }
        st.success(f"{expert} was saved successfully.")

    st.progress(
        len(st.session_state.saved_experts) / len(EXPERTS),
        text=f"Saved expert profiles: {len(st.session_state.saved_experts)} / {len(EXPERTS)}",
    )

with tab_results:
    saved_count = len(st.session_state.saved_experts)

    st.markdown(
        """
        <div class="section-card">
            <h2>Combined analysis and research export</h2>
            <p>
                The final AHP weights are calculated as the normalised average of all saved expert
                profiles. TOPSIS and Sensitivity Analysis are then run using those combined weights.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if saved_count == 0:
        st.warning("Save at least one expert profile in the Expert Assessment tab to generate results.")
    else:
        package = create_results_workbook(st.session_state.saved_experts)

        if package:
            workbook_bytes, final_weights, topsis_df, sensitivity_df = package

            col1, col2, col3 = st.columns(3)
            col1.metric("Saved profiles", f"{saved_count} / {len(EXPERTS)}")
            col2.metric("Ranked techniques", len(topsis_df))
            rank_changes = (sensitivity_df["Ranking Changed?"] == "Yes").sum()
            col3.metric("Sensitivity scenarios with change", int(rank_changes))

            final_df = pd.DataFrame({
                "Criterion": [c["name"] for c in CRITERIA],
                "ID": [c["id"] for c in CRITERIA],
                "Weight": final_weights,
            })

            st.subheader("Combined AHP weights")
            chart_col, table_col = st.columns([1, 1.15])
            with chart_col:
                st.bar_chart(
                    final_df.set_index("ID")[["Weight"]],
                    use_container_width=True,
                )
            with table_col:
                st.dataframe(
                    final_df.style.format({"Weight": "{:.2%}"}),
                    hide_index=True,
                    use_container_width=True,
                )

            st.subheader("TOPSIS ranking")
            ranking_table = topsis_df[
                ["Alternative", "Technique", "Closeness", "Rank"]
            ].sort_values(["Rank", "Alternative"])

            rank_col, rank_chart_col = st.columns([1.35, 1])
            with rank_col:
                st.dataframe(
                    ranking_table.style.format({"Closeness": "{:.3f}"}),
                    hide_index=True,
                    use_container_width=True,
                )
            with rank_chart_col:
                top_chart = ranking_table.sort_values("Closeness").set_index("Alternative")[["Closeness"]]
                st.bar_chart(top_chart, use_container_width=True)

            st.subheader("Sensitivity Analysis")
            sensitivity_display = sensitivity_df.copy()
            st.dataframe(
                sensitivity_display.style.format(
                    {c["id"]: "{:.2%}" for c in CRITERIA}
                ),
                hide_index=True,
                use_container_width=True,
            )

            change_summary = (
                sensitivity_df.groupby("Ranking Changed?")
                .size()
                .rename("Scenarios")
                .to_frame()
            )
            st.subheader("Ranking stability summary")
            st.bar_chart(change_summary, use_container_width=True)

            st.download_button(
                "Download Complete Excel Results",
                data=workbook_bytes,
                file_name="Decentralized_Storage_AHP_TOPSIS_Results.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                type="primary",
                use_container_width=True,
            )

st.markdown(FOOTER_HTML, unsafe_allow_html=True)
