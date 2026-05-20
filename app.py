import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(
    page_title="KRAS CRISPR Dependency Explorer",
    layout="wide"
)

st.title("🧬 KRAS CRISPR Dependency Explorer")
st.markdown("Functional genomics analysis of KRAS-mutant lung cancer vulnerabilities")

# Load data
df = pd.read_csv("results/kras_vs_wt_crispr_hits.csv")

# Clean gene names for display
df["Gene_Symbol"] = df["Gene"].str.replace(r"\s*\(.*\)", "", regex=True)

# Sidebar filters
st.sidebar.header("Filters")

pval_cutoff = st.sidebar.slider(
    "P-value threshold",
    0.0, 0.05, 0.01
)

top_n = st.sidebar.slider(
    "Top genes",
    10, 100, 20
)

filtered = df[df["Pvalue"] <= pval_cutoff]

# -------------------------
# TAB LAYOUT
# -------------------------
tab1, tab2, tab3 = st.tabs([
    "📊 Top Dependencies",
    "🌋 Volcano Plot",
    "🔬 Gene Explorer"
])

# -------------------------
# TAB 1
# -------------------------
with tab1:
    st.subheader("Top KRAS-Associated Vulnerabilities")

    st.dataframe(
        filtered.sort_values("Pvalue").head(top_n)[
            ["Gene_Symbol", "KRAS_mean", "WT_mean", "Diff", "Pvalue"]
        ]
    )

    st.metric("Total Significant Genes", len(filtered))
    st.metric("All Genes Analyzed", len(df))

# -------------------------
# TAB 2
# -------------------------
with tab2:
    st.subheader("Volcano Plot (KRAS vs WT Dependency)")

    fig = px.scatter(
        filtered,
        x="Diff",
        y=-np.log10(filtered["Pvalue"]),
        hover_data=["Gene_Symbol"],
        title="Differential Gene Dependency Landscape"
    )

    st.plotly_chart(fig, use_container_width=True)

# -------------------------
# TAB 3
# -------------------------
with tab3:
    st.subheader("Gene-Level Explorer")

    gene_query = st.text_input("Search gene", "KRAS")

    gene_df = df[df["Gene_Symbol"].str.contains(gene_query, case=False)]

    st.dataframe(gene_df)

    if len(gene_df) > 0:
        st.line_chart(
            gene_df.set_index("Gene_Symbol")["Diff"]
        )
