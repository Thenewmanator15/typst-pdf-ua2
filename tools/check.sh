#!/bin/bash
# check.sh TYPST VERAPDF OUT: compiles every document in documents/one-feature and
# documents/demo.typ as PDF/UA-2 with the given Typst binary into OUT, and validates what
# was exported with veraPDF. A document that the export refuses is listed with its error.
set -uo pipefail
HERE=$(cd "$(dirname "$0")/.." && pwd)
TYPST=$1
VERAPDF=$2
OUT=$3
mkdir -p "$OUT"
files=()
for f in "$HERE"/documents/one-feature/*.typ "$HERE"/documents/demo.typ; do
  b=$(basename "${f%.typ}")
  if "$TYPST" compile --pdf-standard ua-2 "$f" "$OUT/$b.pdf" 2> "$OUT/$b.log"; then
    files+=("$OUT/$b.pdf")
  else
    echo "refused: $b: $(grep '^error' "$OUT/$b.log" | sort -u | cut -c1-100 | tr '
' ' ')"
  fi
done
"$VERAPDF" --flavour ua2 --format json "${files[@]}" > "$OUT/verapdf.json" 2> /dev/null
PYTHON=$(command -v python3 || command -v python)
"$PYTHON" - "$OUT/verapdf.json" <<'EOF'
import json, os, sys
d = json.load(open(sys.argv[1], encoding='utf-8'))
ok = 0
for j in d['report']['jobs']:
    r = j['validationResult']
    r = r[0] if isinstance(r, list) else r
    if r['compliant']:
        ok += 1
    else:
        print('fails:', os.path.basename(j['itemDetails']['name']),
              [(x['clause'], x['failedChecks']) for x in r['details'].get('ruleSummaries', [])])
print(f'conform: {ok} of {len(d["report"]["jobs"])} exported')
EOF
