# bioinformatics_workshop
## Чек сервера
+ pip
+ Miniconda3
+ docker
+ FastQC - отчет о качестве данных
+ SPAdes - для сборки из сырых прочтений
+ RagTag - для сборки псевдохромосом
+ QUAST - для сравнения сборок: определения метрик (N50, количество контигов) и определения количества ошибок (misassemblies).
+ CheckM - для оценки биологической полноты и чистоты сборки

+ базовый метапакет языка программирования R

+ Ragout - (нет, так как требует Python до 3.8) для сборки по множеству референсов (в окружении ragout)

+ OrthoPhylo - для построения деревьев (в окружении orthophylo)

+ BBTools Decontaminate (в окружении bbmap)



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


### Очистка данных (контигов) перед сборкой в скафоолды
Использован инструмент sendsketch.sh из пакета BBTools по команде:
```
sendsketch.sh in=input.fasta out=results_sendsketch/taxonomy.txt
```
Затем, на основе полученного списка сформирован список контигов не принадлежащих анализируемому виду:
```
awk -F'\t' '$2 != 233583 {print $1}' results_sendsketch/taxonomy.txt > contaminants.txt
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

