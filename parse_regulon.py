import re
import os
import json

direc = '/Users/nicolasquach/Documents/stanford/covert_lab/thesis/'
file_name = 'regulon.txt'
save_name = 'transcription.txt'
file = open(os.path.join(direc, file_name), "r")
save_file = open(os.path.join(direc, save_name), "w+")
string = file.read()
#print string
match = re.findall('regulon">(\w+)<', string)
json.dump(match, save_file)
file.close()
save_file.close()