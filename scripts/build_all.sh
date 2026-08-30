#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

python3 scripts/generate_readme.py > README.md
python3 scripts/generate_data_js.py

echo "Done. README.md and docs/data.js are up to date."
