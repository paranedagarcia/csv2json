#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 14:37:06 2018
@author: Patricio Araneda

conn = psycopg2.connect(database='NHL', user='postgres', password='postgres', host='localhost', port='5432')

cat file.json | psql --username=user --password -h localhost -p 5432 database -c "COPY table (jsonb_field) FROM STDIN;"
"""

import sys, getopt
import csv
import json
#import requests
#import psycopg2

csv_file = '/Users/patricio/Downloads/DATOS_MINIMOS.csv'
json_file = 'data.json'


#Get Command Line Arguments
def main(argv):
    csv_file = ''
    json_file = ''

    try:
        opts, args = getopt.getopt(argv,"hi:o:f:",["ifile=","ofile=","format="])
    except getopt.GetoptError:
        print('csv2json.py -i <path to inputfile> -o <path to outputfile> ')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('csv2json.py -i <path to inputfile> -o <path to outputfile> ')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            csv_file = arg
        elif opt in ("-o", "--ofile"):
            json_file = arg
    read_CSV(csv_file, json_file)


#Read CSV File
def read_CSV(csv_file, json_file):
    #csv_rows = []
    with open(csv_file) as csvfile:
    	#reader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_ALL)
        reader = csv.DictReader(csvfile)
        field = reader.fieldnames
        with open(json_file, 'w') as f:
            for row in reader:
                #csv_rows.extend({field[i]:row[field[i]] for i in range(len(field))})
                f.write(json.dumps(
                        {field[i]:row[field[i]] for i in range(len(field))},ensure_ascii=False) +"\n")


if __name__ == "__main__":
   main(sys.argv[1:])

#read_CSV(csv_file, json_file)
