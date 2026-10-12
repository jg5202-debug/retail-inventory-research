# Retail Inventory Research

Inventory growth and subsequent operating performance in selected U.S.-listed merchandise retailers and consumer brands.

The project asks whether inventory growth exceeding revenue growth relates to the following year's gross margin and operating cash flow divided by revenue. It combines cached SEC Company Facts, annual financial panels, accounting reconciliation, OLS models and cited filing reviews.

## Main Results

The manually selected candidate universe contains 42 companies and 656 annual records. The gross-margin sample contains 401 pairs across 36 companies. The OCF-to-revenue sample contains 490 pairs across 42 companies. The common outcome sample contains 399 pairs.

After controlling for the current ratio, revenue growth, log assets, company effects and target-year effects, a 10 percentage-point inventory gap corresponds to:

- Gross margin: -0.1663 percentage points, with a firm-clustered 95% interval of [-0.3491, +0.0164].
- OCF-to-revenue: +0.1955 percentage points, with a firm-clustered 95% interval of [-0.1032, +0.4943].

All eight adjusted sensitivity intervals include zero. The examined specifications do not provide sufficiently precise evidence of a stable association. This does not prove a zero effect or establish predictive performance.

## Read and Present the Project

- [Complete research notebook](notebooks/Retail_Inventory_Research.ipynb)
- [English report](reports/Retail_Inventory_Research_Report.md)
- [Standalone HTML report](reports/Retail_Inventory_Research_Report.html) — download and open locally
- [Presentation](presentation/Retail_Inventory_Research_Presentation.pptx) — English slides with Chinese speaker notes
- [Chinese speaking guide](presentation/Speaker_Guide_CN.md)
- [Teaching Guides for Modules 1–13](guides/)

![Adjusted sensitivity estimates](reports/figures/sensitivity.png)

## Reproduce the Published Report

Use Python 3.12 or newer and a virtual environment. The requirements record the environment used to prepare this version.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/check_snapshot.py
python scripts/render_report.py
```

On Windows, activate the environment with `.venv\Scripts\activate`.
The report script runs only Module 13 using the included processed inputs. It does not download SEC data or refit the regression models.

## Notebook Workflow

The established-project execution order is Modules 1–9, then 12, 10, 11 and 13. Module 12 uses the original Module 11 case-selection file included in the processed data.

For the first execution from an empty data directory, follow the teaching Guides through Module 11 to create the case file, then run Module 12, Module 10, Module 11 and Module 13.

To acquire fresh SEC data, set your own contact before running the acquisition modules:

```bash
export SEC_CONTACT="your.name@example.com"
jupyter lab
```

The notebook finds the project root from the repository or its notebooks/guides directory. The public repository excludes the large raw Company Facts cache. Fresh downloads may change available facts or filing keys, so reconcile review records before comparing versions.

## Module Map

1. Candidate universe and SEC identifiers
2. Pilot financial-data acquisition
3. Annual financial panel
4. Accounting scope and inventory features
5. Current signals and subsequent outcomes
6. Pilot exploratory analysis
7. Expanded sample and coverage screening
8. Missing fields and outcome-specific samples
9. Accounting reconciliation and expanded pairs
10. Expanded exploration and sensitivity
11. Baseline controls and filing-case selection
12. Evidence review and applied sample decisions
13. Final report and reproduction package

## Review Status and Research Limits

This is a completed analysis/report version with partial filing review. Review covers two company eligibility decisions, seven annual rows and three of seven selected cases. Pending cases concern AKA, ARHS, ULTA and KSS. Each statistical outcome sample contains three pairs passing recorded company and three-year scope checks.

The overall sample remains provisional. The candidate universe is manually assembled and histories are unbalanced. Remaining annual missing fields include 42 cost values and 108 gross-profit values. Accounting definitions vary across firms.

Current filings arrive 38–134 days after the target year starts in the retained samples. This retrospective design has no historical point-in-time certification, out-of-sample validation, stock-return backtest or causal identification.

## Data and Sources

Processed inputs and review evidence are under `work/data/processed/`. Source-file hashes are in [the report manifest](reports/source_manifest.json). Raw JSON caches, credentials and local backups are excluded.

- [SEC EDGAR API documentation](https://www.sec.gov/search-filings/edgar-application-programming-interfaces)
- [Gaur, Fisher and Raman (2005), Management Science](https://pubsonline.informs.org/doi/10.1287/mnsc.1040.0298)
- Individual annual-filing citations appear in the report and case-review tables.

The notebook code, comments and report are English. Teaching explanations and presentation speaker notes are Chinese.
