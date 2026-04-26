
> [!WARNING]
> Этот проект всё ещё в разработке. На данный момент в тексте могут отсутствовать важные детали или присутствовать неточности.

# Предисловие
## Задумка

Работа будет состоять из нескольких основных этапов:
- [x] Подготовка исходных данных: проверка качества сборки, аннотация, выделение 16s
- [x] Общий анализ филогении: построение филогенетического дерева
- [ ] Поиск и сравнительный поиск с гомологами генов целлюлаз
- [ ] Предсказание свойств найденных белков
- [ ] Молекулярный докинг для найденных белков с раззличными типами субстратов

## Принцип работы с директориями
Все исходные, промежуточные и итоговые данные хранятся каталогах, которые доступны по ftp. Здесь, на Github присутствуют только основные результаты, если они представлены в виде изображения, короткого текстового файла или таблицы.
Для каждого основного этапа создан свой каталог (и здесь и на ftp сервере):
+ Подготовка исходных данных
+ Общий анализ филогении
+ Поиск и сравнительный поиск с гомологами генов целлюлаз
+ Предсказание свойств найденных белков
+ Молекулярный докинг

Здесь будут описаны общие принципы работы и обоснование тех или иных решений, а также биологические выводы там, где они уместны.
Внутри каждого каталога будет присутствовать свой файл readme.md с "сырыми" шагами - служебные скрипты, команды и т.п. Такая информация создана для удобства, в первую очередь разработчиков.

P.S. в скриптах и командах могут быть не самые корректные пути. В процессе работы структура каталогов немного изменялась для более удобной систематизации данных.

а теперь, после прочтения общих принципов построения работы можно перейти к...
## Резюме

_совсем скоро тут появится резюме проекта, но пока его нет =(_


# Основная часть
## Подготовка исходных данных
> [/2_working_data](2_working_data) - непосредственно подготовка исходных данных

> [!NOTE]
> Таким образом будет даваться ссылка на локальный каталог в репозитории Github **только с результатами** или локальный readme с техническими деталями. Аналогичная структура присутствует и на ftp сервере, но с полными исходными, промежуточными данными и результатами.

Данные для анализа получены из NCBI: использовалась большая часть референсных геномов, которые там представлены для рода _Cellulomonas_.
Получены следующие сборки:

**1. На уровне контигов (contigs)**

   _Cellulomonas algicola_
   
   _Cellulomonas cellasea_
   
   _Cellulomonas composti_
   
   _Cellulomonas hominis_
   
   _Cellulomonas iranensis_
   
   _Cellulomonas pakistanensis_
   
   _Cellulomonas soli_
   
   _Cellulomonas terrae_
   
   _Cellulomonas xylanilytica_
   
**2. На уровне скаффолдов (scaffolds)**
  
   _Cellulomonas fulva_
   
   _Cellulomonas uda_
   
**3. На уровне полного генома (complete)**
   
   _Cellulomonas fimi_
   
   _Cellulomonas flavigena_
   
   _Cellulomonas gilvus_
   
   _Cellulomonas palmilytica_
   
   _Cellulomonas wangleii_
   
   _Cellulomonas wangsupingiae_
   
   _Cellulomonas xiejunii_

Все сборки имеют приемлемый уровень метрик CheckM, но дополнительно был проведен анализ полноты посредством инструмента BUSCO 6.0.0 [1].
> [busco](2_working_data/readme.md#busco) - технические детали
> 
Установлены следующие критерии применимости сборки в дальнейшем анализе:
+ Complete (C) > 95% – основной критерий полноты.
+ Fragmented (F) < 3% – критерий непрерывности сборки.
+ Missing (M) < 3% – дополнительный критерий полноты.
+ Duplicated (D) < 5–10% – чтобы исключить контаминацию или дупликации.


Такие данные были получены для сборок:

| Species | C (%) | S (%) | D (%) | F (%) | M (%) | n |
|---------|-------|-------|-------|-------|-------|---|
| Cellulomonas_algicola | 100.0 | 100.0 | 0.0 | 0.0 | 0.0 | 116 |
| Cellulomonas_cellasea | 98.3 | 97.4 | 0.9 | 0.9 | 0.9 | 116 |
| Cellulomonas_composti | 100.0 | 100.0 | 0.0 | 0.0 | 0.0 | 116 |
| Cellulomonas_fimi | 99.1 | 98.3 | 0.9 | 0.9 | 0.0 | 116 |
| Cellulomonas_flavigena | 99.1 | 97.4 | 1.7 | 0.9 | 0.0 | 116 |
| Cellulomonas_fulva | 100.0 | 100.0 | 0.0 | 0.0 | 0.0 | 116 |
| Cellulomonas_gilvus | 100.0 | 99.1 | 0.9 | 0.0 | 0.0 | 116 |
| Cellulomonas_hominis | 100.0 | 99.1 | 0.9 | 0.0 | 0.0 | 116 |
| Cellulomonas_iranensis | 98.3 | 97.4 | 0.9 | 0.9 | 0.9 | 116 |
| Cellulomonas_pakistanensis | 100.0 | 99.1 | 0.9 | 0.0 | 0.0 | 116 |
| Cellulomonas_palmilytica | 100.0 | 100.0 | 0.0 | 0.0 | 0.0 | 116 |
| Cellulomonas_soli | 98.3 | 98.3 | 0.0 | 0.9 | 0.9 | 116 |
| Cellulomonas_terrae | 99.1 | 98.3 | 0.9 | 0.9 | 0.0 | 116 |
| Cellulomonas_uda | 100.0 | 100.0 | 0.0 | 0.0 | 0.0 | 116 |
| Cellulomonas_wangleii | 100.0 | 100.0 | 0.0 | 0.0 | 0.0 | 116 |
| Cellulomonas_wangsupingiae | 100.0 | 100.0 | 0.0 | 0.0 | 0.0 | 116 |
| Cellulomonas_xiejunii | 99.1 | 99.1 | 0.0 | 0.9 | 0.0 | 116 |
| Cellulomonas_xylanilytica | 95.7 | 95.7 | 0.0 | 1.7 | 2.6 | 116 |

Аннотация выполнена посредством Bakta 1.12.0 [2] с использованием эталонной базы данных версии 6.0 (схема 6, релиз от 24 февраля 2025 г.) [3]
> [bakta](2_working_data/readme.md#bakta) - технические детали

> [!CAUTION]
> **ТУТ СЛЕДУЕТ ДОПИСАТЬ**

Для дальнейшего этапа (построения филогенетического дерева) выбрана последовательность 16s рРНК в силу достаточной консервативновти, удобства поиска и анализа. 
Конечно, для высокой точности определения степени филогенетического родства видов, выделившихся не так давно, консервативность 16s может стать проблемой. Более целесообразным могли бы стать другие методы, например использование полного оперона рРНК или мультилокусный анализ последовательностей.
Первый неприменим в силу наличия последовательностей с низким уровнем сборки, второй - как один из более сложных вариантов - будет применён позже (возможно).  
Для выделения 16s из последовательностей использовался инструмент barrnap 0.9 [4]. Он предназначен для быстрого предсказания генов рибосомальной РНК в бактериальных, архейных и эукариотических геномах. 
> [barrnap](2_working_data/readme.md#barrnap) - технические детали

## Общий анализ филогении: построение филогенетического дерева
> [/3_phylogenetic_tree](3_phylogenetic_tree) - построение дерева

Подготовка данных и филогенетический анализ выполнялись в MEGA 12.1.2 [5]. 
Первым делом вручную (для выбора конкретных последовательностей из набора) был создан multifasta файл.

Готовый файл выровнен с применением алгоритма MUSCLE на следующих параметрах:
> Gap Open 400,00  
> Gap Extend 0,00  
> Max Memory in MB 24576  
> Max Iterations 16  
> Cluster Method (Iterations 1,2) UPGMA  
> Cluster Method (Other Iterations) UPGMA  
> Min Diag Length (Lambda) 24

Тримминг концов не выполнялся.

Для построения дерева подобрана наилучшая модель, выбранная на основе байесовского информационного критерия, который определён функцией "поиск моделей" (Find Best DNA/Protein Models) в MEGA для 24 вариантов: T92+G+I (модель Тамуры с Гамма распрелением и инвариантными сайтами).
> [Поиск моделей - таблица с результатами](3_phylogenetic_tree/2_process_data/2_method)

Параметры подбора модели:
> Statistical Method Maximum Likelihood  
> Tree to Use Automatic (Neighbor-joining tree)  
> Approach Full (slow)  
> Substitutions Type Nucleotide  
> Gaps/Missing Data Partial deletion  
> Site Coverage Cutoff (%) 80  
> Select Codon Positions 1st, 2nd, 3rd, Noncoding Sites  
> Branch Swap Filter Strong

После подбора модели выполнено построение дерева на следующих параметрах:
> Method: Maximum Likelihood Tree
> Statistical Method Maximum Likelihood
> Test of Phylogeny Standard Bootstrap (slow)
> Bootstrap Replicates 1000
> Substitutions Type Nucleotide
> Model/Method Tamura-Nei model
> Rates among Sites Gamma Distributed With Invariant Sites (G+I)
> No of Discrete Gamma Categories 5
> Gaps/Missing Data Partial deletion
> Site Coverage Cutoff (%) 80
> Select Codon Positions 1st, 2nd, 3rd, Noncoding sites
> ML Heuristic Method Nearest-Neighbor-Interchange (NNI)
> Initial Tree for ML Make initial tree automatically (Default - NJ/MP)
> Branch Swap Filter Strong
> Number of Threads 16

> [!CAUTION]
> **ТУТ СЛЕДУЕТ ДОПИСАТЬ**

Вот подготовленные таблицы:

---

### Метрики качества

| Метрика | Значение |
|---------|----------|
| Log-likelihood (LnL) | –3858.591 |
| AICc | 7801.309 |
| BIC | 8148.297 |
| Суммарная длина ветвей (Sum of branch lengths) | 0.174 |
| Доля инвариантных сайтов (Invar) | 0.8656 (86.56%) |
| Параметр гамма-распределения (Gamma) | 0.6527 |
| Соотношение транзиций/трансверсий (Ts/Tv) | 1.538 |
| Модель замещений | Tamura-Nei 1993 (+G+I) |
| Количество параметров | 42 |
| Количество сайтов | 1515 |
| Количество таксонов | 19 |

## Bootstrap поддержки узлов (в долях)

| Клада | Bootstrap |
|--------------|-----------|
| (Cellulomonas gilvus, Cellulomonas fulva) | 0.975 |
| (Cellulomonas palmilytica, Cellulomonas uda) | 0.996 |
| ((C. gilvus, C. fulva), (C. palmilytica, C. uda)) | 1.000 |
| (Cellulomonas flavigena, Cellulomonas wangleii) | 0.956 |
| (Cellulomonas iranesis, Cellulomonas xiejunii) | 0.942 |
| ((C. flavigena, C. wangleii), (C. iranesis, C. xiejunii)) | 0.925 |
| (C. wangsupingiae, предыдущий кластер) | 1.000 |
| (Cellulomonas algicola, Cellulomonas fimi) | 0.979 |
| (Cellulomonas cellasea, Sanguibacter suarezii) | 0.969 |
| ((C. algicola, C. fimi), (C. cellasea, Sanguibacter)) | 0.904 |
| Крупный внутренний узел (объединяющий C. wangsupingiae и др.) | 0.948 |
| (Cellulomonas xylanilytica, (C. hominis, C. pakistanensis)) | 0.798 |
| (Cellulomonas hominis, Cellulomonas pakistanensis) | 1.000 |
| Cellulomonas soli (отдельная ветвь) | 0.833 |
| Корневой узел (весь остаток дерева) | 0.845 |


## Результаты
_и неменого биологических выводов_

## Ссылки
1. metashot/busco: Nextflow. metashot, 2026.
2. Schwengers O. и др. Bakta: rapid & standardized annotation of bacterial genomes via alignment-free sequence identification: Python // Microbial Genomics. 2021.
3. Schwengers O. Bakta database. Zenodo, 2025.
4. Seemann T. tseemann/barrnap: Perl. 2026.
5. Kumar S, Stecher G, Suleski M, Sanderford M, Sharma S, and Tamura K (2024) Molecular Evolutionary Genetics Analysis Version 12 for adaptive and green computing. Molecular Biology and Evolution 41:1-9.



## Платформы
_здесь будет указано основное железо и платформы (если сервис размещен онлайн)_
