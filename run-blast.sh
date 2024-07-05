#! /bin/bash

set -e # exit script on error

for var in $2
  do
    echo "Running BLAST for ${var}..."
    blastn \
        -db db/${var} \
        -query $1 \
        -word_size 9 \
        -gapopen 3 \
        -gapextend 2\
        -num_threads 4 \
        -reward 1 \
        -penalty -1 \
        -out "${3}/results_${var}.xml" \
        -outfmt 5
  done