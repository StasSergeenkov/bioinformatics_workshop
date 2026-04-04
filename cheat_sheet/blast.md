```
/mnt/hgfs/SFTP/4_cellulases_analysis/
```
созданы базы данных для каждого вида на основе аннотации:
```
for faa in *.faa; do
    base=$(basename $faa .faa)
    makeblastdb -in $faa -dbtype prot -out 0_blast/${base}
done
```
