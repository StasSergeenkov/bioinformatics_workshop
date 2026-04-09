#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Paths
BASE_DIR = "/mnt/hgfs/SFTP/4_cellulases_analysis"
BLAST_RESULTS = os.path.join(BASE_DIR, "3_blast_results")

# Load data
presence = pd.read_csv(os.path.join(BLAST_RESULTS, "blast_presence_matrix.csv"), index_col=0)
best_hits = pd.read_csv(os.path.join(BLAST_RESULTS, "blast_best_hits.csv"))
summary = pd.read_csv(os.path.join(BLAST_RESULTS, "blast_summary_counts.csv"))

# Rename columns for better labels
presence.columns = ['GH9 (AAW62376.2)', 'Xylanase (ABD96969.1)', 'EG (AAD48494.3)']

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 150

# ==================== 1. Presence heatmap ====================
plt.figure(figsize=(6, 10))
sns.heatmap(presence, annot=True, cmap='Blues', cbar=False, linewidths=0.5,
            fmt='d', square=True, annot_kws={'size': 12})
plt.title('Presence of reference cellulases in Cellulomonas genomes', fontsize=14)
plt.ylabel('Genome', fontsize=12)
plt.xlabel('Reference protein', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(BLAST_RESULTS, "heatmap_presence.png"), dpi=300)
plt.close()

# ==================== 2. Clustered heatmap ====================
sns.clustermap(presence, annot=True, cmap='Blues', fmt='d',
               figsize=(6, 10), cbar=False, linewidths=0.5,
               annot_kws={'size': 12})
plt.savefig(os.path.join(BLAST_RESULTS, "clustermap_presence.png"), dpi=300)
plt.close()

# ==================== 3. Bar chart of gene counts ====================
summary_sorted = summary.sort_values('num_ref_hits', ascending=False)
colors = ['#2c7bb6' if x == 3 else '#fdae61' if x == 2 else '#d7191c' for x in summary_sorted['num_ref_hits']]

plt.figure(figsize=(10, 6))
plt.bar(summary_sorted['genome'], summary_sorted['num_ref_hits'], color=colors)
plt.xticks(rotation=45, ha='right', fontsize=9)
plt.ylabel('Number of reference cellulases found', fontsize=12)
plt.xlabel('Genome', fontsize=12)
plt.title('Cellulase gene content per genome (based on 3 markers)', fontsize=14)
plt.ylim(0, 3.5)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(os.path.join(BLAST_RESULTS, "barplot_counts.png"), dpi=300)
plt.close()

# ==================== 4. Bubble chart for GH9 ====================
gh9 = best_hits[best_hits['qseqid'] == 'AAW62376.2'].copy()
if not gh9.empty:
    gh9 = gh9.sort_values('pident', ascending=False)
    plt.figure(figsize=(10, 6))
    plt.scatter(gh9['genome'], gh9['pident'], s=gh9['bitscore']/5, alpha=0.7, c='green', edgecolors='black')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Percent identity to GH9 reference', fontsize=12)
    plt.xlabel('Genome')
    plt.title('Quality of GH9 homologs across Cellulomonas genomes')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(BLAST_RESULTS, "bubble_gh9.png"), dpi=300)
    plt.close()
else:
    print("No GH9 hits found, skipping bubble chart.")

# ==================== 5. Heatmap of percent identity ====================
pivot_pident = best_hits.pivot_table(index='genome', columns='qseqid', values='pident', aggfunc='max')
if not pivot_pident.empty:
    plt.figure(figsize=(6, 10))
    sns.heatmap(pivot_pident, annot=True, fmt='.0f', cmap='YlOrBr',
                cbar_kws={'label': 'Max % identity'}, linewidths=0.5)
    plt.title('Best percent identity to reference cellulases')
    plt.tight_layout()
    plt.savefig(os.path.join(BLAST_RESULTS, "heatmap_pident.png"), dpi=300)
    plt.close()
else:
    print("No pident data for heatmap.")

print("All plots saved to:", BLAST_RESULTS)