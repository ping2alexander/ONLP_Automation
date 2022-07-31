import yaml
from yaml.loader import SafeLoader
from datetime import datetime
import random

data=dict()
index_table_time = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
RegId = random.randint(10000, 100000)

with open('index_var.yml', 'r') as f1:
    data = yaml.load(f1, Loader=SafeLoader)

data['Index']['Entries'].append({'Date_Time': index_table_time, 'RegId': RegId}) 

with open('index_var.yml', 'w') as f2:
    yaml.dump(data, f2)

