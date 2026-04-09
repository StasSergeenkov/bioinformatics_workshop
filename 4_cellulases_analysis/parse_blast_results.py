#!/usr/bin/env python3

import pandas as pd
import os

# Paths
BASE_DIR = "/mnt/hgfs/SFTP/4_cellulases_analysis"
RAW_BLAST = os.path.join(BASE_DIR, "3_blast_results/all_blast_raw.tsv")
OUTPUT_DIR = os.path.join(BASE_DIR, "3_blast_results")

# Read raw BLAST results
df = pd.read_csv(RAW_BLAST, sep='\t')

# Keep only best hit per (query, genome) based on bitscore
best_hits = df.sort_values('bitscore', ascending=False).drop_duplicates(subset=['qseqid', 'genome'])

# Presence matrix: 1 if hit exists
presence_matrix = best_hits.pivot_table(index='genome', columns='qseqid', aggfunc='size', fill_value=0)
presence_matrix = (presence_matrix > 0).astype(int)

# Save files
presence_matrix.to_csv(os.path.join(OUTPUT_DIR, "blast_presence_matrix.csv"))
best_hits.to_csv(os.path.join(OUTPUT_DIR, "blast_best_hits.csv"), index=False)

summary = best_hits.groupby('genome')['qseqid'].count().reset_index()
summary.columns = ['genome', 'num_ref_hits']
summary.to_csv(os.path.join(OUTPUT_DIR, "blast_summary_counts.csv"), index=False)

print("Analysis finished. Results in:", OUTPUT_DIR)
