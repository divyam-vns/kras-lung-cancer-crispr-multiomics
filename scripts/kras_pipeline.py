
# KRAS CRISPR Dependency Analysis Pipeline

import pandas as pd
from scipy.stats import ttest_ind

crispr = pd.read_csv("data/raw/CRISPRGeneEffect.csv", low_memory=False)
models = pd.read_csv("data/raw/Model.csv")
mutations = pd.read_csv("data/raw/OmicsSomaticMutations.csv", low_memory=False)

kras = mutations[mutations["HugoSymbol"] == "KRAS"]
lung_models = models[models["OncotreeLineage"] == "Lung"]

kras_ids = kras["ModelID"].unique()

kras_lung = lung_models[lung_models["ModelID"].isin(kras_ids)]
wt_lung = lung_models[~lung_models["ModelID"].isin(kras_ids)]

kras_crispr = crispr[crispr["ModelID"].isin(kras_lung["ModelID"])]
wt_crispr = crispr[crispr["ModelID"].isin(wt_lung["ModelID"])]

genes = crispr.columns[1:]

results = []

for g in genes:
    try:
        k = kras_crispr[g].dropna()
        w = wt_crispr[g].dropna()

        if len(k) > 2 and len(w) > 2:
            stat, p = ttest_ind(k, w)

            results.append([
                g,
                k.mean(),
                w.mean(),
                k.mean() - w.mean(),
                p
            ])
    except:
        continue

res = pd.DataFrame(results, columns=[
    "Gene","KRAS_mean","WT_mean","Diff","Pvalue"
])

res.to_csv("results/kras_crispr_results.csv", index=False)
print("Pipeline complete")
