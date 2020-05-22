import csv
import json
import requests
import datetime
import os


with open('lista.csv',  encoding='ISO-8859-1' ) as csvfile:
    reader = csv.DictReader(csvfile)
    rfcAnterior = '';
    for row in reader:
        print (row)