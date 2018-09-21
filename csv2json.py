#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 14:37:06 2018
@author: Patricio Araneda
"""
import sys, getopt
import csv
import json

csv_file = '/Users/patricio/Downloads/DATOS_MINIMOS.csv'
json_file = 'data.json'

#datetime_end = datetime.datetime.now()
#datetime_start = datetime_end - datetime.timedelta(days=365)

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
            print('csv_json.py -i <path to inputfile> -o <path to outputfile> ')
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
