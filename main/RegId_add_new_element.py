import yaml
from yaml.loader import SafeLoader
from datetime import datetime
from datetime import date
import sys
import os.path as path
import importlib

filename = sys.argv[2]

parentdir = path.abspath(path.join(__file__,"../.."))
tmppath = parentdir + '/tmp'
sys.path.insert(1, tmppath)
DUTsInfo = importlib.import_module(filename)

RegId = sys.argv[1]
Results = 'href="http://172.22.92.133/' + RegId + '/' + 'Results"'
log = 'href="http://172.22.92.133/' + RegId + '/' + 'log"'

with open('regId_var.yml', 'r') as f1:
    data = yaml.load(f1, Loader=SafeLoader)

data['RegId']['Results'] = Results
data['RegId']['log'] = log

with open('regId_var.yml', 'w') as f2:
    yaml.dump(data, f2)

