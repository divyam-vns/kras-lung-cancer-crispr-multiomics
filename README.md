
# KRAS-Mutant Lung Cancer CRISPR Dependency Analysis
## Overview

This project performs a functional genomics analysis of KRAS-mutant non-small cell lung cancer (NSCLC) using large-scale CRISPR-Cas9 gene dependency data combined with somatic mutation profiles and cancer cell line metadata.

The goal is to identify genetic vulnerabilities specific to KRAS-mutant lung cancer cells, enabling insights into potential therapeutic targets and synthetic lethal interactions.

## Objectives
Identify KRAS-mutant vs wild-type lung cancer cell lines
Quantify genome-wide gene essentiality differences
Detect KRAS-specific dependency signatures
Perform statistical differential dependency analysis
Visualize vulnerabilities using volcano plots
Interpret functional pathways using enrichment analysis

## Biological Rationale

KRAS is one of the most frequently mutated oncogenes in lung adenocarcinoma and remains a challenging therapeutic target.
KRAS-driven tumors exhibit:

- Increased metabolic rewiring
- Dependency on stress response pathways
- Synthetic lethal vulnerabilities in DNA repair and ribosome biogenesis pathways

This study leverages CRISPR-Cas9 loss-of-function screening data to uncover these dependencies.

## Datasets Used
Dataset	Description	Source

- CRISPRGeneEffect.csv	- Gene knockout dependency scores across cancer - cell lines	- DepMap
- Model.csv	- Cancer cell line metadata (tissue, subtype, annotations) -	DepMap
- OmicsSomaticMutations.csv -	Somatic mutation profiles including KRAS status -	DepMap

## Workflow Summary
1. Data Integration
Loaded CRISPR dependency matrix
Integrated mutation and model metadata
Harmonized ModelID across datasets
2. Cohort Definition
Defined KRAS-mutant NSCLC cell lines
Defined KRAS wild-type NSCLC controls
3. Gene Dependency Analysis
Compared CRISPR gene knockout effects
Computed mean dependency scores per group
4. Statistical Testing
Performed two-sample t-tests
Calculated p-values and effect sizes
5. Differential Dependency Ranking
Ranked genes by:
effect size (KRAS vs WT)
statistical significance (-log10 p-value)
6. Visualization
Volcano plot of gene dependency landscape
Highlighted KRAS and top candidate vulnerabilities
7. Pathway Enrichment (GSEA)
Ranked gene list input into enrichment analysis
Identified disrupted biological pathways

## Key Findings
KRAS itself shows strong dependency signal, validating pipeline sensitivity
Ribosomal proteins show strong differential essentiality
Stress response and translation regulation pathways are enriched
Several uncharacterized genes show KRAS-specific lethality signatures
KRAS-mutant cells show distinct vulnerability landscape compared to WT

## Example Results

Top differentially essential genes:
```
KRAS
RPL6
PSMF1
RPL23
TCP1
DHX8
```
These genes suggest:

- Translational dependency
- Proteostasis stress
- Oncogene-driven metabolic rewiring

## Output Figure
```
Volcano plot showing differential gene dependency
X-axis: effect size (KRAS vs WT)
Y-axis: statistical significance (-log10 p-value)
```
## Biological Interpretation

KRAS-mutant lung cancer cells exhibit:

Increased dependency on ribosome biogenesis
Enhanced proteostasis stress response requirements
Potential synthetic lethal interactions with translation machinery
Vulnerabilities in chromatin regulation pathways

These findings align with known KRAS oncogenic rewiring mechanisms.

## Technologies Used
```
Python (Pandas, NumPy, SciPy)
Statistical testing (t-test)
Matplotlib / Seaborn (visualization)
GSEApy (pathway analysis)
Google Colab (execution environment)
Git / GitHub (version control)
```
## Repository Structure
```
kras-lung-cancer-crispr-multiomics/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── scripts/
│   ├── data_preprocessing.py
│   ├── differential_dependency.py
│   ├── visualization.py
│   ├── gsea_analysis.py
│
├── results/
│   ├── volcano_plot.png
│   ├── ranked_genes.csv
│
├── notebooks/
│   ├── KRAS_CRISPR_pipeline.ipynb
│
└── README.md

```
## Reproducibility

To reproduce the analysis:
```
git clone https://github.com/divyam-vns/kras-lung-cancer-crispr-multiomics.git
cd kras-lung-cancer-crispr-multiomics
pip install -r requirements.txt
```
Then run:
```
python scripts/differential_dependency.py
```
## Future Directions
Integrate RNA-seq expression data
Add drug sensitivity (PRISM / GDSC)
Build predictive ML model for KRAS vulnerability
Extend to multi-cancer KRAS dependency mapping
Build interactive Streamlit dashboard
## Impact

This workflow demonstrates:

Functional interpretation of CRISPR screening data
Multi-omics integration in cancer biology
Identification of actionable therapeutic vulnerabilities
Reproducible computational oncology pipeline
## Author

Dr. Divya Mishra, Ph.D.
Bioinformatics / Genomics Data Science Project
KRAS Functional Dependency Analysis — Lung Cancer
