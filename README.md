# csv2json
Pyhton command line program to convert csv files into json files, one line for record aka Mongodb format. This format is required to import to PostgreSQL jsonb field.

[![DOI](https://zenodo.org/badge/149786445.svg)](https://zenodo.org/badge/latestdoi/149786445)

## How to use
Make csv2json.py executable with:
```
sudo chmod +x csv2json.py
```
To execute use arguments file_csv and file_json.
```
-i to identified csv file (the input file)
-o to identified json file (the output file)
```
The command line must be:
```
csv2json.py -i file_csv -o file.json
```
The json file contains a line for each record without comma separation.
```
{"id":"DIR","nombre":"Director","detalle":"Director de Laboratorio"}
{"id":"LBM","nombre":"Lab. Manager","detalle":"Administrador de Laboratorio"}
{"id":"LAB","nombre":"Laboratorio","detalle":"Personal de Laboratorio"}
{"id":"USR","nombre":"Usuario Externo","detalle":"Usuario externo"}
{"id":"INV","nombre":"Usuario","detalle":"Investigador asociado a un proyecto"}
```
To import this file into PostgreSQL jsonb field use:
```
cat file.json | psql --username=user --password -h localhost -p 5432 database -c "COPY table (jsonb_field) FROM STDIN;"
```
