import re
 
log_file_path = (r"rawdata-beacond-lga13-1349-12003.log.19")
regex = '("protocol": "https")'
print(log_file_path)
match_list = []
with open(log_file_path, "r") as file:
    for line in file:
        print(line[0:220])
        break
        # for match in re.finditer(regex, line, re.S):
        #     match_text = match.group()
        #     match_list.append(match_text)
        #     print (match_text)