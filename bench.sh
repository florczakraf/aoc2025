#!/bin/bash
set -Eeuo pipefail

N=5

for s in $(find . -name '*py' | sort); do
    if [ -f "$s.stats" ]; then
        cat "$s.stats"
        continue
    fi

    interpreter=$(head -n 1 "$s" | rev | cut -d" " -f 1 | rev)
    echo -ne "| [$s]($s) | $interpreter | " >> "$s.stats"
    totals=()
    for _ in $(seq 1 $N); do
        d=$(dirname "$s")
        start=$(date +%s%N)
        "$s" < "$d/input" >/dev/null
        total_ms="$((($(date +%s%N) - "$start")/1000000))"
        totals+=("$total_ms")
        echo -n "${total_ms}"$'\u00a0'ms" | " >> "$s.stats"
    done

    # we discard slowest and fastest run from the average
    avg=$(python3 -c "import sys; l=[int(x) for x in sys.argv[1:]]; l.remove(min(l)); l.remove(max(l)); print(sum(l)//len(l))" "${totals[@]}")
    echo "**${avg}"$'\u00a0'"ms** |" >> "$s.stats"

    cat "$s.stats"
done
