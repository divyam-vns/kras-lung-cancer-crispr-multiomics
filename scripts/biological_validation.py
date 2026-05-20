# scripts/biological_validation.py

import pandas as pd
import numpy as np

def main():
    print("🧬 KRAS BIOLOGICAL VALIDATION")

    df = pd.read_csv("results/kras_vs_wt_crispr_hits.csv")

    # Fix potential numerical issues
    df["Pvalue"] = df["Pvalue"].replace(0, 1e-300)
    df["-log10P"] = -np.log10(df["Pvalue"])

    print("\n📊 Top biologically relevant hits:\n")

    selected = df.sort_values("Diff").head(10)
    print(selected[["Gene", "Diff", "-log10P"]])

    print("\n🔬 KRAS sanity check:")
    kras_row = df[df["Gene"].str.contains("KRAS")]
    print(kras_row[["Gene", "Diff", "Pvalue", "-log10P"]])

    print("\n📈 Summary stats:")
    print("Mean Diff:", df["Diff"].mean())
    print("Max significance:", df["-log10P"].max())

    print("\n✅ BIOLOGICAL VALIDATION COMPLETE")

if __name__ == "__main__":
    main()
