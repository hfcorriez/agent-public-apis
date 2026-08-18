#!/usr/bin/env bash
# Drive the harvest/verify pipeline.
#   ./verify.sh           re-probe data/apis.json (100% live, ≥400)
#   ./verify.sh --refresh re-harvest sources, probe, regenerate docs
set -u
ROOT="$(cd "$(dirname "$0")" && pwd)"
if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is required" >&2
  exit 2
fi
if ! command -v curl >/dev/null 2>&1; then
  echo "curl is required" >&2
  exit 2
fi
if [[ "${1:-}" == "--refresh" || "${1:-}" == "refresh" ]]; then
  exec python3 "$ROOT/scripts/pipeline.py" refresh
fi
exec python3 "$ROOT/scripts/pipeline.py" verify
