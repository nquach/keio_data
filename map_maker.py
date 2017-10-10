import numpy as np
import openpyxl as xls
import json
import os

direc = '/Users/nicolasquach/Documents/stanford/covert_lab/thesis/'

lyso_hits_file_name = 'lyso_hits.txt'
lysis_hits_file_name = 'lysis_hits.txt'

lyso_file = open(os.path.join(direc, lyso_hits_file_name), 'r')
lysis_file = open(os.path.join(direc, lysis_hits_file_name), 'r')

lyso_dict = json.load(lyso_file)
lysis_dict = json.load(lysis_file)

lyso_file.close()
lysis_file.close()

positions = []

for key in sorted(lyso_dict.keys()):
	positions.append(key)

for key in sorted(lysis_dict.keys()):
	positions.append(key)

letters = ['A','B','C','D','E','F','G','H']
numbers = range(1,13)

pos_list = []

for letter in letters:
	for num in numbers:
		pos_str = letter + str(num)
		pos_list.append(pos_str)

plate1 = positions[0:96]
plate2 = positions[96:192]
plate3 = positions[192:288]

wb = xls.load_workbook('map.xlsx')
sheet1 = wb.get_sheet_by_name('Plate1')
sheet2 = wb.get_sheet_by_name('Plate2')
sheet3 = wb.get_sheet_by_name('Plate3')

for index in range(0,96):
	pos = pos_list[index]
	sheet1[pos] = plate1[index]
	sheet2[pos] = plate2[index]
	sheet3[pos] = plate3[index]

wb.save('map.xlsx')



