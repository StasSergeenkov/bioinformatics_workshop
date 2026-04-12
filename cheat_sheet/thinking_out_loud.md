# bioinformatics_workshop
## Чек сервера
+ pip
+ Miniconda3
+ docker
+ FastQC - отчет о качестве данных
+ SPAdes - для сборки из сырых прочтений
+ RagTag - для сборки псевдохромосом (в окружении base)
+ QUAST - для сравнения сборок: определения метрик (N50, количество контигов) и определения количества ошибок (misassemblies). (в окружении base)
+ CheckM - для оценки биологической полноты и чистоты сборки (в окружении checkm)

+ базовый метапакет языка программирования R

+ Ragout - (нет, так как требует Python до 3.8) для сборки по множеству референсов (в окружении ragout)

+ OrthoPhylo - для построения деревьев (в окружении orthophylo)

+ BBTools Decontaminate (в окружении bbmap)

+ BUSCO - для оценки полноты сборки генома, набора генов или транскриптома (в окружении busco)
+ Bakta - аннотатор (в окружении bakta)
+ Prokka 1.14.5 (в окружении prokka145)
+ Prokka 1.15.6 (в окружении prokka156)
+ Barrnap 0.9 (в окружении barrnap)
+ seqkit (в окружении barrnap)
+ esearch 24.0 - это набор UNIX-команд для доступа к базам данных NCBI (в окружении edirect)
+ blast (в окружении edirect)
+ pandas (в окружении edirect)
+ python 3.14 (в окружении edirect)
+ python 3.10 (в окружении viz)
+ matplotlib (в окружении edirect и viz)
+ seaborn (в окружениях edirect и viz)


## Подготовка исходных данных
### Оценка качества данных

| Название вида | Референс | Сборка | RefSeq | GenBank | Используется | Уровень сборки | CheckM Completeness (полнота) | CheckM Contamination (загрязнение) | Scaffold/Contig N50 | Ссылка |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|*Cellulomonas xylanilytica*|Да|ASM798980v1|GCF_007989805.1|GCA_007989805.1|GenBank| Contig |98.41%|1.73%|293.8 kb|[Ссылка](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_007989805.1/)|
| *Cellulomonas uda* | Да | ASM1175968v1 | GCF_011759685.1 | GCA_011759685.1 | GenBank | Scaffold | 96.94% | 0.70% | 715.5 kb | [Ссылка](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_011759685.1/) |
| *Cellulomonas terrae* | Да | ASM799026v1 | GCF_007990265.1 | GCA_007990265.1 | GenBank | Contig | 99.12% | 2.68% | 145.3 kb | [Ссылка](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_007990265.1/) |
| *Cellulomonas fimi* | Да | ASM21269v1 | GCF_000212695.1 | GCA_000212695.1 | GenBank | Complete Genome | 99.77% | 0.39% | 4.3 Mb | [Ссылка](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000212695.1/) |
| *Cellulomonas gilvus* | Да | ASM21854v1 | GCF_000218545.1 | GCA_000218545.1 | GenBank | Complete Genome | 99.82% | 0.39% | 3.5 Mb | [Ссылка](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000218545.1/) |
| *Cellulomonas flavigena* | Да | ASM9286v1 | GCF_000092865.1 | GCA_000092865.1 | GenBank | Complete Genome | 98.66% | 0.27% | 4.1 Mb | [Ссылка](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000092865.1/) |
| *Cellulomonas xiejunii* | Да | ASM2450831v1 | GCF_024508315.1 | GCA_024508315.1 | GenBank | Complete Genome | 99.06% | 1.07% | 4.2 Mb | [Ссылка](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_024508315.1/) |
| *Cellulomonas wangsupingiae* | Да | ASM2450827v1 | GCF_024508275.1 | GCA_024508275.1 | GenBank | Complete Genome | 97.67% | 1.74% | 4.1 Mb | [Ссылка](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_024508275.1/) |
| *Cellulomonas wangleii* | Да | ASM1838844v1 | GCF_018388445.1 | GCA_018388445.1 | GenBank | Complete Genome | 97.57% | 1.75% | 4.1 Mb | [Ссылка](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_018388445.1/) |
| *Cellulomonas palmilytica* | Да | ASM2159004v1 | GCF_021590045.1 | GCA_021590045.1 | GenBank | Complete Genome | 98.85% | 1.05% | 3.8 Mb | [Ссылка](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_021590045.1/) |
| *Cellulomonas iranensis* | Да | ASM3081473v1 | GCF_030814735.1 | GCA_030814735.1 | GenBank | Contig | 98.35% | 3.92% | 4.0 Mb | [Ссылка](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_030814735.1/) |
| *Cellulomonas cellasea* | Да | ASM653874v1 | GCF_006538745.1 | GCA_006538745.1 | GenBank | Contig | 97.54% | 2.73% | 194.5 kb | [Ссылка](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_006538745.1/) |
| *Cellulomonas soli* | Да | ASM1340930v1 | GCF_013409305.1 | GCA_013409305.1 | GenBank | Contig | 98.31% | 2.76% | 4.3 Mb | [Ссылка](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_013409305.1/) |
| *Cellulomonas algicola* | Да | ASM1902430v1 | GCF_019024305.1 | GCA_019024305.1 | GenBank | Contig | 99.34% | 2.03% | 273.9 kb | [Ссылка](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_019024305.1/) |
| *Cellulomonas pakistanensis* | Да | ASM1686275v1 | GCF_016862755.1 | GCA_016862755.1 | GenBank | Contig | 96.45% | 5.53% | 117.2 kb | [Ссылка](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_016862755.1/) |
| *Cellulomonas composti* | Да | ASM799024v1 | GCF_007990245.1 | GCA_007990245.1 | GenBank | Contig | 96.73% | 0.68% | 234.3 kb | [Ссылка](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_007990245.1/) |
| *Cellulomonas fulva* | Да | ASM1853137v1 | GCF_018531375.1 | GCA_018531375.1 | GenBank | Scaffold | 98.85% | 2.55% | 3.1 Mb | [Ссылка](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_018531375.1/) |
| *Cellulomonas hominis* | Да | ASM1891780v1 | GCF_018917805.1 | GCA_018917805.1 | GenBank | Contig | 96.92% | 4.47% | 420.7 kb | [Ссылка](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_018917805.1/) |


Cellulomonas gilvus - использовался в качестве референса для сборки псевдохромосом


### Сборка скаффолдов
Для коррекции
```bash
ragtag correct reference.fasta contigs.fasta -o corrected
```
Затем, на основе полученных данных произведена сборка скаффолдов:
```bash
ragtag scaffold reference.fasta corrected/ragtag.correct.fasta -o scaffolded
```

Последующая оценка качества полученных данных включала в себя:
```bash
quast.py Cellulomonas_xylanilytica.fasta scaffolded/ragtag.scaffold.fasta \
    -r reference_gilvus.fasta \
    -o quast_comparison \
    --gene-finding
```
Для проверки CheckM:
```bash
#Предварительно необходимо создать каталог bins и перенести туда сборку:
mkdir -p bins
cp scaffolded/ragtag.scaffold.fasta bins/

#а затем запускать анализ
checkm taxonomy_wf -x fasta -t 8 -f results.txt genus Cellulomonas bins/ output_checkm/
```
Дополнительно подготовим графики:
```bash
#GC plot
checkm gc_plot -x fasta --image_type pdf bins/ gc_plots/ 100

#Coding plot
checkm coding_plot -x fasta --image_type pdf output_checkm/ bins/ coding_plots/ 100
```

Также через BUSCO (сохранение результатов в домашнюю директорию, так как он дурак):
```bash
busco -i /mnt/hgfs/SFTP/assembling/Cellulomonas_xylanilytica/Cellulomonas_xylanilytica.fasta \
      -o busco_result_assembling \
      -m genome \
      -l /home/stas/busco_data/busco_downloads/lineages/bacteria_odb12 \
      --out_path /home/stas/busco_results/two \
      -c 8 \
      -f \
      --offline
```


**Массовое выполнение (run_busco_all.sh)**
```bash
#!/bin/bash
set -e  # остановка при любой ошибке

BASE_DATA="/mnt/hgfs/SFTP/working_data"
BUSCO_TMP="/home/stas/busco_results"

# Список штаммов (все, кроме fimi)
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
        echo "Ошибка: файл $INPUT_FASTA не найден! Пропускаем."
        continue
    fi

    # Подготовка временной папки
    rm -rf "$BUSCO_TMP"
    mkdir -p "$BUSCO_TMP"

    # Запуск BUSCO
    busco -i "$INPUT_FASTA" \
          -o "busco_result_${strain##*_}" \
          -m genome \
          -l /home/stas/busco_data/busco_downloads/lineages/bacteria_odb12 \
          --out_path "$BUSCO_TMP" \
          -c 4 \
          -f \
          --offline

    # Копирование результатов в исходный каталог
    cp -r "$BUSCO_TMP" "$BASE_DATA/$strain/"

    # Удаление временной папки
    rm -rf "$BUSCO_TMP"

    echo "$strain завершён"
    echo
done

echo "Все операции выполнены."
```
**Парсинг данных (parse_busco_summary.sh)**
```bash
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

# Заголовок
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

    # Ищем строку, содержащую "C:" (например, C:98.3%[S:98.3%,D:0.0%],F:0.9%,M:0.9%,n:116)
    line=$(grep -m1 "C:" "$summary_file")
    if [ -z "$line" ]; then
        echo "Предупреждение: не найдена строка с результатами в файле: $summary_file" >&2
        echo "| $strain | - | - | - | - | - | - |" >> "$OUTPUT"
        continue
    fi

    # Парсим значения с помощью sed (учитываем, что проценты могут быть без дробной части)
    C_val=$(echo "$line" | sed -n 's/.*C:\([0-9.]*\)%.*/\1/p')
    S_val=$(echo "$line" | sed -n 's/.*S:\([0-9.]*\)%.*/\1/p')
    D_val=$(echo "$line" | sed -n 's/.*D:\([0-9.]*\)%.*/\1/p')
    F_val=$(echo "$line" | sed -n 's/.*F:\([0-9.]*\)%.*/\1/p')
    M_val=$(echo "$line" | sed -n 's/.*M:\([0-9.]*\)%.*/\1/p')
    n_val=$(echo "$line" | sed -n 's/.*n:\([0-9]*\).*/\1/p')

    # Если какие-то значения не извлеклись, ставим прочерк
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
Аннотация Bakta:
```
bakta --db /home/stas/bakta_db/db \
      --output /home/stas/annotation_results \
      --prefix my_genome \
      --threads 8 \
      --verbose \
      /path/to/your/genome.fasta
```

### Сборка псевдохромосом из скаффолдов
в RagTag команда:
```
ragtag.py scaffold reference.fasta scaffolds.fasta -o ragtag_output -u -r
```
reference.fasta — референсный геном 
scaffolds.fasta — исходные скаффолды
-o ragtag_output — папка, куда будут сохранены результаты
-u — добавляет суффикс к названиям последовательностей (полезно, чтобы не перепутать с исходными)
-r — принуждает RagTag оценивать размеры гэпов (пробелов) между контигами на основе выравнивания на референс, а не просто вставлять стандартные 100 пар оснований

### Построение дерева
**укоренение**
по геному Sanguibacter suarezii NBRC 16159
[https://pmc.ncbi.nlm.nih.gov/articles/PMC1081325/figure/f1/]

Процессы:
1. Получение 16s
   ```shell
   mkdir -p barrnap_results && \
   barrnap --kingdom bac --threads 4 \
   --outseq barrnap_results/rrna_sequences.fasta \
   входной_файл.fna > barrnap_results/rrna_predictions.gff
   ```

**множественное выполнение run_barrnap.sh** (создание скрипта)
```shell
# 1. Удалить старый скрипт (если есть)
rm -f /home/stas/run_barrnap.sh

# 2. Создать новый скрипт с исправленным содержимым
cat > /home/stas/run_barrnap.sh << 'EOF'
#!/bin/bash
# Скрипт для извлечения 16S рРНК из сборок Cellulomonas и Sanguibacter
# Исправлена фильтрация: поиск по "16S" без учёта регистра

set -e  # остановка при ошибке

# Корневая директория с данными
ROOT="/mnt/hgfs/SFTP/2_working_data"

# Список видов (имена подкаталогов)
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
    echo "ОШИБКА: seqkit не установлен. Установите: conda install -c bioconda seqkit"
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
        echo "  Файл $INPUT_FASTA не найден, пропускаем"
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
        echo "  ВНИМАНИЕ: временный FASTA-файл пуст. Проверьте barrnap."
        continue
    fi
    
    echo "  Временный FASTA содержит $(grep -c '^>' "$TMP_ALL") последовательностей"
    
    # Фильтрация 16S (ищем "16S" в заголовке, регистронезависимо)
    echo "  Фильтрация 16S..."
    seqkit grep -r -i -p "16S" "$TMP_ALL" > "$OUT_FASTA"
    
    COUNT_16S=$(grep -c '^>' "$OUT_FASTA" 2>/dev/null || echo 0)
    echo "  Найдено 16S последовательностей: $COUNT_16S"
    
    # Удаляем временный файл
    rm -f "$TMP_ALL"
    
    if [ "$COUNT_16S" -eq 0 ]; then
        echo "  ПРЕДУПРЕЖДЕНИЕ: не найдено ни одной 16S последовательности для $sp"
    fi
    
    echo "  Результаты сохранены в $OUT_DIR"
    echo "----------------------------------------"
done

echo "Готово."
EOF

# 3. Сделать скрипт исполняемым
chmod +x /home/stas/run_barrnap.sh

# 4. Запустить скрипт
/home/stas/run_barrnap.sh
```
2. Создание мульти-фаста
3. Выравнивание (стандартные настройки MEGA, алгоритм MUSCLE)
4. Подбор модели: лучшая модель: T92+G+I
5. Построение дерева по модели

