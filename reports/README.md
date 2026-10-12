# Retail Inventory Research: Final Deliverable

Report date: 2026-10-11
Scope: retrospective operating-performance associations with partial filing review.

## Files
- Retail_Inventory_Research_Report.html: standalone report with embedded figures.
- Retail_Inventory_Research_Report.md: editable report; keep the figures directory beside it.
- figures/: model comparison, descriptive group means, and adjusted sensitivity intervals.
- source_manifest.json: relative input paths and SHA-256 hashes for this report version.

## Reproduction
Use the existing project root and cached SEC data. Required libraries are pandas, matplotlib, requests, numpy, statsmodels, and IPython.
The completed notebook preserves the earlier modules and their outputs, and appends the executed report module.
Its established-project execution order is Modules 1-9, 12, 10, 11, 13. Module 12 uses the initial Module 11 case file already present in the project.
For a fresh project, first follow the original Guides through Module 11 to create inputs and the initial case file; then run Module 12, Module 10, Module 11, and Module 13.
Set PROJECT_ROOT for your machine. Update REPORT_DATE when generating a new report version.
After changing manual review CSVs, run Module 12 to apply decisions, Modules 10 and 11 to refresh analyses, and all eight Module 13 cells to rebuild the report.
Module 13 alone reads saved inputs; it does not acquire data, audit filings, or refit models.
The version checks intentionally stop reporting if saved analyses or manual decisions are stale.

## Completed and Remaining Work
The analysis/report deliverable is complete for this snapshot. Full historical filing review, prediction validation, and causal identification are not complete.
Reviewed cases: 3 of 7. Pending selected cases: AKA, ARHS, ULTA, KSS.
The report records pending work and does not fabricate supporting evidence or fill unapproved values.
