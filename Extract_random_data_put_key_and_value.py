import re
import json


log_file_path = (r"rawdata-beacond-lga13-1349-12003.log.19")
regex = '("protocol": "https")'
print(log_file_path)
match_list = []
all_list = []
keys = [] 
values = []
with open(log_file_path, "r") as file:
    for line in file:
        new_line = line
        all_list.append(new_line)
        line = json.loads(line[1:])
        print(type(line))
        items = line.items() 
        for item in items: 
            keys.append(item[0]), values.append(item[1]) 
        
        # printing keys and values separately 
        print ("keys : ", str(keys)) 
        print ("values : ", str(values))

        #testing
        break
        # for match in re.finditer(regex, line, re.S):
        #     match_text = match.group()
        #     match_list.append(match_text)
        #     print (match_text)
#split dictionary into keys and values 
