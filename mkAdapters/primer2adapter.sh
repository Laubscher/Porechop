#!/bin/bash

fasta="$1"
set_name="Adapter_set"

revcomp() {
    echo "$1" | tr "ACGTacgt" "TGCAtgca" | rev
}

while read -r line; do
  if [[ "$line" == ">"* ]]; then
    name="${line#>}"
  else
    seq="$line"
    rc=$(revcomp "$seq")
    echo "Adapter('${set_name}_${name}', start_sequence=('${name}_start', '$seq'), end_sequence=('${name}_end', '$rc')),"
  fi
done < "$fasta"

