# scripts/verify_deployment_safety.py

import pandas as pd

def main():
    print("🧬 KRAS DEPLOYMENT SAFETY CHECK")

    df = pd.read_csv("results/kras_vs_wt_crispr_hits.csv")

    print("\n📊 Dataset Shape:", df.shape)
    print("\n📌 Columns:", df.columns.tolist())

    print("\n🧹 Missing values (total):", df.isnull().sum().sum())

    print("\n🔝 Top 5 genes by significance:")
    top = df.sort_values("Pvalue").head(5)
    print(top[["Gene", "Diff", "Pvalue"]])

    # Safety checks
    assert "Gene" in df.columns, "Missing Gene column"
    assert "Pvalue" in df.columns, "Missing Pvalue column"
    assert df.shape[0] > 1000, "Dataset too small — likely broken load"

    print("\n✅ SAFETY CHECK PASSED — Streamlit ready!")

if __name__ == "__main__":
    main()
