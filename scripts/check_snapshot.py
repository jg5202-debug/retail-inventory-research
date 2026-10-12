"""Verify input-file hashes for the published research report."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "reports/source_manifest.json").read_text())
for source in manifest["sources"]:
    path = root / source["path"]
    assert hashlib.sha256(path.read_bytes()).hexdigest() == source["sha256"], str(path)
print("Verified", len(manifest["sources"]), "report inputs.")
print("Sample status:", manifest["sample_status"])
