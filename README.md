# csv2json
Pyhton command line program to convert csv files into json files, one line for record aka Mongodb format. This format is required to import to PostgreSQL jsonb field.

## How to use
Make csv2json.py executable with:
 sudo chmod +x csv2json.py
To execute use arguments file_csv and file_json. 
-i to identified csv file (the input file)
-o to identified json file (the output file)
 csv2json.py -i file_csv -o file.json
