import re
import json
import pandas as pd


log_file_path = (r"rawdata-beacond-lga13-1349-12003.log.19")
regex = '("protocol": "https")'
print(log_file_path)
df = pd.DataFrame(index=None)
df2 = pd.DataFrame(index=None)
with open(log_file_path, "r") as file:
    for line in file:
        line = json.loads(line[1:])
        items = line.items() 
        #df.append(pd.Series([line]), ignore_index=True)
        #df = df.append(pd.DataFrame.from_records([line], index=[0])) 
        df = df.append(pd.DataFrame.from_dict([line]))
        df.append(df, ignore_index=True)
        #df = pd.DataFrame([line], index=list(range(0, len(line))))
        #print(df.head())
        break
print("work")
#df = pd.DataFrame([all_list], index=line(range(0, len(all_list)))) 
print(df.head())
