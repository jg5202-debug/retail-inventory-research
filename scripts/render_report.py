"""Rebuild the final report from included processed inputs, without network calls."""
import json
import os
from pathlib import Path
import matplotlib

matplotlib.use("Agg")
root = Path(__file__).resolve().parents[1]
os.chdir(root)
notebook = json.loads((root / "notebooks/Retail_Inventory_Research.ipynb").read_text())
namespace = {"__name__": "__main__"}
in_report_module = False
count = 0
for cell in notebook["cells"]:
    source = "".join(cell["source"])
    if cell["cell_type"] == "markdown" and source.startswith("## Module 13:"):
        in_report_module = True
    elif in_report_module and cell["cell_type"] == "code":
        exec(compile(source, "Module13", "exec"), namespace)
        count += 1
assert count == 8, "Expected eight report cells."
print("Report rebuilt in", root / "reports")
