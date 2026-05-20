import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(
    page_title="KRAS CRISPR Explorer",
    layout="wide"
)

st.title("🧬 KRAS CRISPR Dependency Explorer")

st.markdown("""
Interactive dashboard for exploring
KRAS-mutant lung cancer vulnerabilities
using CRISPR dependency data.
""")

# Load data
df = pd.read_csv("results/ranked_genes.csv")

# Create logP if missing
if "logP" not in df.columns:
    df["logP"] = -np.log10(df["Pvalue"])

# Sidebar
st.sidebar.header("Filters")

pval_cutoff = st.sidebar.slider(
    "P-value cutoff",
    0.0,
    0.05,
    0.01
)

filtered = df[df["Pvalue"] <= pval_cutoff]

# Top genes
st.subheader("Top Differential Dependencies")

st.dataframe(
    filtered.sort_values("Pvalue").head(20)
)

# Volcano Plot
st.subheader("Volcano Plot")

fig = px.scatter(
    filtered,
    x="Diff",
    y="logP",
    hover_name="Gene",
    title="KRAS vs WT Dependency Landscape"
)

st.plotly_chart(fig, use_container_width=True)

# Gene Search
st.subheader("Gene Search")

gene = st.text_input(
    "Enter Gene Name",
    "KRAS"
)

gene_df = df[
    df["Gene"].str.contains(
        gene,
        case=False,
        na=False
    )
]

st.dataframe(gene_df)

# Summary stats
st.subheader("Dataset Summary")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Genes",
    len(df)
)

col2.metric(
    "Significant Genes",
    len(filtered)
)

col3.metric(
    "Top Hit",
    filtered.sort_values("Pvalue").iloc[0]["Gene"]
    if len(filtered) > 0 else "N/A"
)
