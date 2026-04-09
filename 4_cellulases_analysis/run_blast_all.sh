#!/bin/bash

# Директории
BASE_DIR="/mnt/hgfs/SFTP/4_cellulases_analysis"
QUERY="${BASE_DIR}/1_original_data/1_reference/reference_proteins.faa"
DB_DIR="${BASE_DIR}/1_original_data/0_blast"
OUTPUT_DIR="${BASE_DIR}/3_blast_results"
TEMP_DIR="${BASE_DIR}/2_process_data"

# Создаём выходные папки
mkdir -p "$OUTPUT_DIR" "$TEMP_DIR"

# Файл для объединённых результатов (сырой BLAST)
RAW_OUTPUT="${OUTPUT_DIR}/all_blast_raw.tsv"

# Заголовок для raw-файла
echo -e "qseqid\tsseqid\tpident\tlength\tmismatch\tgapopen\tqstart\tqend\tsstart\tsend\tevalue\tbitscore\tgenome" > "$RAW_OUTPUT"

# Цикл по всем базам (файлы .phr в папке 0_blast)
for db in ${DB_DIR}/*.phr; do
    # Извлекаем имя базы (без расширения .phr) — это название вида
    db_base=$(basename "$db" .phr)
    genome_name="${db_base}"
    
    echo "Processing $genome_name..."
    
    # Временный файл для вывода BLAST по этому геному
    tmp_file="${TEMP_DIR}/${genome_name}_blast.tmp"
    
    blastp -query "$QUERY" -db "${DB_DIR}/${db_base}" \
        -outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore" \
        -evalue 1e-10 -num_threads 4 -out "$tmp_file"
    
    # Добавляем колонку с именем генома и объединяем
    awk -v genome="$genome_name" '{print $0 "\t" genome}' "$tmp_file" >> "$RAW_OUTPUT"
    
    # Удаляем временный файл
    rm "$tmp_file"
done

echo "BLAST завершён. Результаты сохранены в $RAW_OUTPUT"