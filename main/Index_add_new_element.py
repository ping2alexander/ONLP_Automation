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

data=dict()
index_table_date = date.today().strftime("%B %d, %Y")
index_table_time = datetime.now().strftime("%H:%M:%S")
RegId = sys.argv[1]
Server= sys.argv[3]
Page = '"http://' + Server + '/' + RegId + '"'

with open('index_var.yml', 'r') as f1:
    data = yaml.load(f1, Loader=SafeLoader)

data['Index']['Entries'].append({'Date': index_table_date, 'Time': index_table_time, 'Platform': DUTsInfo.DUT1_Label_Revision,'RegId': RegId, 'Page': Page}) 

with open('index_var.yml', 'w') as f2:
    yaml.dump(data, f2)

