# Технические пояснения к шагу
## busco
Проверка качества сборки выполнена следующей командой (частный пример): 
```shell
busco -i /mnt/hgfs/SFTP/assembling/Cellulomonas_xylanilytica/Cellulomonas_xylanilytica.fasta \
      -o busco_result \
      -m genome \
      -l /home/stas/busco_data/busco_downloads/lineages/bacteria_odb12 \
      --out_path /home/stas/busco_results/two \
      -c 8 \
      -f \
      --offline
```
Для массового выполнения во всех каталогах со всеми последовательностями использован bash-скрипт:
```shell
#!/bin/bash
set -e  # остановка при любой ошибке

BASE_DATA="/mnt/hgfs/SFTP/working_data"
BUSCO_TMP="/home/stas/busco_results"
# мой сервер дурак и поэтому диркетория находится в корневой директории пользователя

STRAINS=(
    Cellulomonas_algicola
    Cellulomonas_fimi
    Cellulomonas_cellasea
    Cellulomonas_composti
    Cellulomonas_flavigena
    Cellulomonas_fulva
    Cellulomonas_gilvus
    Cellulomonas_hominis
    Cellulomonas_iranensis
    Cellulomonas_pakistanensis
    Cellulomonas_palmilytica
    Cellulomonas_soli
    Cellulomonas_terrae
    Cellulomonas_uda
    Cellulomonas_wangleii
    Cellulomonas_wangsupingiae
    Cellulomonas_xiejunii
    Cellulomonas_xylanilytica
)

for strain in "${STRAINS[@]}"; do
    echo "=========================================="
    echo "Обработка: $strain"
    echo "=========================================="

    INPUT_FASTA="$BASE_DATA/$strain/$strain.fasta"
    if [ ! -f "$INPUT_FASTA" ]; then
        echo "Ошибка: файл $INPUT_FASTA не найден! Пропускаю..."
        continue
    fi

    rm -rf "$BUSCO_TMP"
    mkdir -p "$BUSCO_TMP"

    busco -i "$INPUT_FASTA" \
          -o "busco_result_${strain##*_}" \
          -m genome \
          -l /home/stas/busco_data/busco_downloads/lineages/bacteria_odb12 \
          --out_path "$BUSCO_TMP" \
          -c 4 \
          -f \
          --offline

    cp -r "$BUSCO_TMP" "$BASE_DATA/$strain/"

    rm -rf "$BUSCO_TMP"

    echo "$strain завершён"
    echo
done

echo "Все операции выполнены."
```
А затем, для удобства дальнейшего анализа, все данные были собраны в одну таблицу следующим скриптом:

```shell
#!/bin/bash

BASE="/mnt/hgfs/SFTP/working_data"
OUTPUT="$BASE/busco_analysis_summary.txt"

STRAINS=(
    Cellulomonas_algicola
    Cellulomonas_cellasea
    Cellulomonas_composti
    Cellulomonas_fimi
    Cellulomonas_flavigena
    Cellulomonas_fulva
    Cellulomonas_gilvus
    Cellulomonas_hominis
    Cellulomonas_iranensis
    Cellulomonas_pakistanensis
    Cellulomonas_palmilytica
    Cellulomonas_soli
    Cellulomonas_terrae
    Cellulomonas_uda
    Cellulomonas_wangleii
    Cellulomonas_wangsupingiae
    Cellulomonas_xiejunii
    Cellulomonas_xylanilytica
)

echo "| Species | C (%) | S (%) | D (%) | F (%) | M (%) | n |" > "$OUTPUT"
echo "|---------|-------|-------|-------|-------|-------|---|" >> "$OUTPUT"

for strain in "${STRAINS[@]}"; do
    suffix="${strain##*_}"
    summary_file="$BASE/$strain/busco_results/busco_result_$suffix/short_summary.specific.bacteria_odb12.busco_result_$suffix.txt"

    if [ ! -f "$summary_file" ]; then
        echo "Предупреждение: файл не найден: $summary_file" >&2
        echo "| $strain | - | - | - | - | - | - |" >> "$OUTPUT"
        continue
    fi

    line=$(grep -m1 "C:" "$summary_file")
    if [ -z "$line" ]; then
        echo "Предупреждение: не найдена строка с результатами в файле: $summary_file" >&2
        echo "| $strain | - | - | - | - | - | - |" >> "$OUTPUT"
        continue
    fi

    C_val=$(echo "$line" | sed -n 's/.*C:\([0-9.]*\)%.*/\1/p')
    S_val=$(echo "$line" | sed -n 's/.*S:\([0-9.]*\)%.*/\1/p')
    D_val=$(echo "$line" | sed -n 's/.*D:\([0-9.]*\)%.*/\1/p')
    F_val=$(echo "$line" | sed -n 's/.*F:\([0-9.]*\)%.*/\1/p')
    M_val=$(echo "$line" | sed -n 's/.*M:\([0-9.]*\)%.*/\1/p')
    n_val=$(echo "$line" | sed -n 's/.*n:\([0-9]*\).*/\1/p')

    [ -z "$C_val" ] && C_val="-"
    [ -z "$S_val" ] && S_val="-"
    [ -z "$D_val" ] && D_val="-"
    [ -z "$F_val" ] && F_val="-"
    [ -z "$M_val" ] && M_val="-"
    [ -z "$n_val" ] && n_val="-"

    echo "| $strain | $C_val | $S_val | $D_val | $F_val | $M_val | $n_val |" >> "$OUTPUT"
done

echo "Готово. Результат сохранён в $OUTPUT"
```


## bakta

Аннотация выполнена командой (в общем виде):
```shell
bakta --db /home/stas/bakta_db/db \
      --output /home/stas/annotation_results \
      --prefix my_genome \
      --threads 8 \
      --verbose \
      /path/to/your/genome.fasta
```
Для массового выполнения во всех каталогах со всеми последовательностями использован bash-скрипт (создание и запуск скрипта):
```shell

```
> [!CAUTION]
> **ТУТ СЛЕДУЕТ ДОПИСАТЬ**



## barrnap

Получение всех рРНК для конкретного организма выполнено командой:

```shell
mkdir -p barrnap_results && \
barrnap --kingdom bac --threads 4 \
--outseq barrnap_results/rrna_sequences.fasta \
входной_файл.fna > barrnap_results/rrna_predictions.gff
```

Для массового выполнения во всех каталогах со всеми последовательностями, а также выборки из результатов анализа конкретно 16s рРНК использован bash-скрипт (создание и запуск скрипта):

```shell
cat > /home/stas/run_barrnap.sh << 'EOF'
#!/bin/bash

set -e  # остановка при ошибке

# Корневая директория с данными
ROOT="/mnt/hgfs/SFTP/2_working_data"

# Список подкаталогов с данными
SPECIES=(
    "Cellulomonas_algicola"
    "Cellulomonas_cellasea"
    "Cellulomonas_composti"
    "Cellulomonas_fimi"
    "Cellulomonas_flavigena"
    "Cellulomonas_fulva"
    "Cellulomonas_gilvus"
    "Cellulomonas_hominis"
    "Cellulomonas_iranensis"
    "Cellulomonas_pakistanensis"
    "Cellulomonas_palmilytica"
    "Cellulomonas_soli"
    "Cellulomonas_terrae"
    "Cellulomonas_uda"
    "Cellulomonas_wangleii"
    "Cellulomonas_wangsupingiae"
    "Cellulomonas_xiejunii"
    "Cellulomonas_xylanilytica"
    "Sanguibacter_suarezii"
)

# Проверка наличия seqkit
if ! command -v seqkit &> /dev/null; then
    echo "ОШИБКА: seqkit не установлен!"
    exit 1
fi

# Цикл по видам
for sp in "${SPECIES[@]}"; do
    echo "=== Обработка: $sp ==="
    
    # Пути
    SP_DIR="${ROOT}/${sp}"
    INPUT_FASTA="${SP_DIR}/${sp}.fasta"
    OUT_DIR="${SP_DIR}/barrnap_results"
    
    # Проверка существования входного файла
    if [ ! -f "$INPUT_FASTA" ]; then
        echo "  Файл $INPUT_FASTA не найден, пропускаю..."
        continue
    fi
    
    # Создание выходной директории
    mkdir -p "$OUT_DIR"
    
    # Временные и выходные файлы
    TMP_ALL="${OUT_DIR}/${sp}_all_rrna.tmp"
    OUT_FASTA="${OUT_DIR}/${sp}_16s.fasta"
    OUT_GFF="${OUT_DIR}/${sp}.gff"
    
    echo "  Запуск barrnap..."
    barrnap --kingdom bac --threads 4 --outseq "$TMP_ALL" "$INPUT_FASTA" > "$OUT_GFF"
    
    # Проверка, что временный файл создан и не пуст
    if [ ! -s "$TMP_ALL" ]; then
        echo "  ВНИМАНИЕ: временный FASTA-файл пуст!"
        continue
    fi
    
    echo "  Временный FASTA содержит $(grep -c '^>' "$TMP_ALL") последовательностей"
    
    # Фильтрация 16S (поиск "16S" в заголовке, регистронезависимо)
    echo "  Фильтрация 16S..."
    seqkit grep -r -i -p "16S" "$TMP_ALL" > "$OUT_FASTA"
    
    COUNT_16S=$(grep -c '^>' "$OUT_FASTA" 2>/dev/null || echo 0)
    echo "  Найдено 16S последовательностей: $COUNT_16S"
    
    # Удаляем временный файл
    rm -f "$TMP_ALL"
    
    if [ "$COUNT_16S" -eq 0 ]; then
        echo "  ПРЕДУПРЕЖДЕНИЕ: не найдено ни одной 16S последовательности для $sp !"
    fi
    
    echo "  Результаты сохранены в $OUT_DIR"
    echo "----------------------------------------"
done

echo "Скрипт завершил работу."
EOF

chmod +x /home/stas/run_barrnap.sh
/home/stas/run_barrnap.sh
```
