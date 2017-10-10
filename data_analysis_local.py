import json
import os
import numpy as np
import xlrd as xls

plate_numbers = ['1_1','1_2', 3, 5, 7, '9_1','9_2', 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 39, 41, 43, 45, 47, 49, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 89, 95]
direc = '/Users/nicolasquach/Documents/stanford/covert_lab/thesis/'

#[title, total_cells, num_infected, num_uninfected, num_lytic, num_lyso, mode, var]
def get_OD_data(plate_numbers):
	direc = '/Users/nicolasquach/Documents/stanford/covert_lab/thesis/'
	data_direc = os.path.join(direc, 'platereader')
	save_direc = os.path.join(direc, 'datatxt')
	compiled_file_path = os.path.join(save_direc, 'OD_data.txt')
	compiled_file = open(compiled_file_path, 'w+')
	compiled_dict = {}
	letters = ['A','B','C','D','E','F','G','H']
	numbers = range(1,13)
	positions = []
	for letter in letters:
		for number in numbers:
			pos = letter + str(number)
			positions.append(pos)

	for plate_number in plate_numbers:
		print plate_number
		plate_dict = {}
		file_name = 'keio' + str(plate_number) + '.xls'
		file_path = os.path.join(data_direc, file_name)
		wb = xls.open_workbook(file_path)
		sheet = wb.sheet_by_index(0)
		for i in range(0,96):
			pos = positions[i]
			plate_dict[pos] = sheet.cell_value(rowx=i+1, colx=5)

		compiled_dict[plate_number] = plate_dict
	
	json.dump(compiled_dict, compiled_file)
	compiled_file.close()


def compile_dataset(direc, plate_numbers):
	dataset = {}
	compiled_file_name = 'all_data.txt'
	compiled_file = open(os.path.join(direc, compiled_file_name), "w+")
	for plate_number in plate_numbers:
		print 'Adding Keio ' + str(plate_number)
		file_name = 'keio' + str(plate_number) + '.txt'
		plate_file = open(os.path.join(direc, file_name), 'r')
		plate_dict = json.load(plate_file)
		plate_dict = invert_plate_index(plate_dict)
		dataset[plate_number] = [plate_dict]
		plate_file.close()

	json.dump(dataset, compiled_file)
	compiled_file.close()

#[title, total_cells, num_infected, num_uninfected, num_lytic, num_lyso, mode, var]

def compile_dataset_by_name(direc, plate_numbers):
	dataset = {}
	compiled_file_name = 'data_by_name.txt'
	compiled_file = open(os.path.join(direc, compiled_file_name), "w+")
	for plate_number in plate_numbers:
		print 'Adding Keio ' + str(plate_number)
		file_name = 'keio' + str(plate_number) + '.txt'
		plate_file = open(os.path.join(direc, file_name), 'r')
		plate_dict = json.load(plate_file)
		plate_dict = invert_plate_index(plate_dict)
		for pos in plate_dict.keys():
			stats_list = plate_dict[pos]
			title = stats_list[0]
			total_cells = stats_list[1]
			num_infected = stats_list[2]
			num_uninfected = stats_list[3]
			num_lytic = stats_list[4]
			num_lyso = stats_list[5]
			mode = stats_list[6]
			var = stats_list[7]
			pos_str = 'K' + str(plate_number) + pos
			dataset[title] = [pos_str, total_cells, num_infected, num_uninfected, num_lytic, num_lyso, mode, var]
		plate_file.close()

	json.dump(dataset, compiled_file)
	compiled_file.close()

def load_name_dataset(direc):
	compiled_file_name = 'data_by_name.txt'
	compiled_file = open(os.path.join(direc, compiled_file_name), "r")
	compiled_data = json.load(compiled_file)
	compiled_file.close()
	return compiled_data

def load_maynard_hits(direc):
	file_name = 'maynard_hits.txt'
	file = open(os.path.join(direc, file_name), "r")
	data = json.load(file)
	file.close()
	return data

def load_transcription_f(direc):
	file_name = 'transcription.txt'
	file = open(os.path.join(direc, file_name), "r")
	data = json.load(file)
	file.close()
	return data

def add_plates(direc, plate_numbers):
	compiled_file_name = 'all_data.txt'
	compiled_file = open(os.path.join(direc, compiled_file_name), "w+")
	dataset = json.load(compiled_file)
	for plate_number in plate_numbers:
		print 'Adding Keio ' + str(plate_number)
		file_name = 'keio' + str(plate_number) + '.txt'
		plate_file = open(os.path.join(direc, file_name), 'r')
		plate_dict = json.load(plate_file)
		plate_dict = invert_plate_index(plate_dict)
		dataset[plate_number] = plate_dict
		plate_file.close()

	json.dump(dataset, compiled_file)
	compiled_file.close()

def load_dataset(direc):
	compiled_file_name = 'all_data.txt'
	compiled_file = open(os.path.join(direc, compiled_file_name), "r")
	compiled_data = json.load(compiled_file)
	compiled_file.close()
	return compiled_data

def load_OD_data(direc):
	data_file_name = 'OD_data.txt'
	data_file = open(os.path.join(direc, data_file_name), 'r')
	data = json.load(data_file)
	data_file.close()
	return data

def invert_index(old_index):
	letter = old_index[0]
	old_num = int(old_index[1:])
	new_num = str(13 - old_num)
	new_index = letter + new_num
	return new_index

def invert_plate_index(old_dict):
	new_dict = {}
	for key in old_dict.keys():
		new_key = invert_index(key)
		new_dict[new_key] = old_dict[key]
	return new_dict

def print_data(direc, plate = None):
	dataset = load_dataset(direc)
	OD_data = load_OD_data(direc)
	for plate_num in sorted(dataset.keys()):
		#print plate_num == plate
		if plate != None and str(plate) != str(plate_num):
			continue
		else:
			plate_dict = dataset[plate_num][0]
			OD_dict = OD_data[plate_num]
			print 'Data for Keio ' + str(plate_num)
			for pos in sorted(plate_dict.keys()):
				stats_list = plate_dict[pos]
				#print stats_list
				OD = OD_dict[pos]
				title = stats_list[0]
				total_cells = stats_list[1]
				num_infected = stats_list[2]
				num_uninfected = stats_list[3]
				num_lytic = stats_list[4]
				mode = stats_list[6]
				var = stats_list[7]
				if num_infected+num_uninfected > 0:
					frac_infected = float(num_infected)/float(num_infected+num_uninfected)
				else:
					frac_infected = 0
				if title != None:
					pos_str = 'K' + str(plate_num) + pos + ': ' + title
					print pos_str + ' mode=' + str(mode) + ' n_lytic=' + str(num_lytic) + ' infected=' + str(num_infected) + ' total cells=' + str(num_infected+num_uninfected) + ' frac_infected=' + str(frac_infected) + ' OD600=' + str(OD)

def filter_hits(name = None, mode_lb = 0.0, mode_ub = 1.0, n_infected_lb = 0, n_infected_ub = 10000, n_cell_lb = 0, n_cell_ub = 10000, frac_infected_lb = 0, frac_infected_ub = 1.0, var_lb = 0, var_ub = 10000, n_lytic_lb = 0, n_lytic_ub = 10000, n_lyso_lb = 0, n_lyso_ub = 10000, OD_lb = 0, OD_ub = 1, in_maynard = False, is_TF = False, save_hits = False, save_name = 'hits.txt'):
	print ' '
	hits = {}
	counter = 0
	if name != None:
		dataset = load_name_dataset(direc)
		stats_list = dataset[name]
		counter += 1
		pos_str = stats_list[0]
		total_cells = stats_list[1]
		num_infected = stats_list[2]
		num_uninfected = stats_list[3]
		num_lytic = stats_list[4]
		mode = stats_list[6]
		var = stats_list[7]
		if num_infected+num_uninfected > 0:
			frac_infected = float(num_infected)/float(total_cells)
		else:
			frac_infected = 0
		print pos_str + ' ' + name + ' mode=' + str(mode) + ' n_lytic=' + str(num_lytic) + ' infected=' + str(num_infected) + ' total cells=' + str(num_infected+num_uninfected) + ' frac_infected=' + str(frac_infected) 
	else:
		dataset = load_dataset(direc)
		OD_data = load_OD_data(direc)
		for plate_num in sorted(dataset.keys()):
			plate_dict = dataset[plate_num][0]
			OD_dict = OD_data[plate_num]
			#print 'Hits for Keio ' + str(plate_num)
			for pos in sorted(plate_dict.keys()):
				stats_list = plate_dict[pos]
				#print stats_list
				OD = OD_dict[pos]
				title = stats_list[0]
				total_cells = stats_list[1]
				num_infected = stats_list[2]
				num_uninfected = stats_list[3]
				num_lytic = stats_list[4]
				num_lyso = stats_list[5]
				mode = stats_list[6]
				var = stats_list[7]
				if num_infected+num_uninfected > 0:
					frac_infected = float(num_infected)/float(total_cells)
				else:
					frac_infected = 0

				if title != None:
					maynard_hits = load_maynard_hits(direc)
					transcription_f = load_transcription_f(direc)
					pos_str = 'K' + str(plate_num) + pos + ': ' + title
					mode_criteria = (mode >= mode_lb) and (mode <= mode_ub)
					n_infected_criteria = (num_infected >= n_infected_lb) and (num_infected <= n_infected_ub)
					n_cell_criteria = (total_cells >= n_cell_lb) and (total_cells <= n_cell_ub)
					frac_infected_criteria = (frac_infected >= frac_infected_lb) and (frac_infected <= frac_infected_ub)
					var_criteria = (var >= var_lb) and (var <= var_ub)
					lytic_criteria = (num_lytic >= n_lytic_lb) and (num_lytic <= n_lytic_ub)
					lyso_criteria = (num_lyso >= n_lyso_lb) and (num_lyso <= n_lyso_ub)
					OD_criteria = (OD >= OD_lb) and (OD <= OD_ub)
					maynard_criteria = True
					TF_criteria = True
					if in_maynard:
						maynard_criteria = title in maynard_hits
					if is_TF:
						TF_criteria = title.lower() in (name.lower() for name in transcription_f)
					criteria_met = mode_criteria and n_infected_criteria and n_cell_criteria and frac_infected_criteria and var_criteria and lytic_criteria and lyso_criteria and OD_criteria and maynard_criteria and TF_criteria
					if criteria_met:
						counter += 1
						print pos_str + ' mode=' + str(mode) + ' n_lytic=' + str(num_lytic) + ' infected=' + str(num_infected) + ' total cells=' + str(num_infected+num_uninfected) + ' frac_infected=' + str(frac_infected) + ' OD600=' + str(OD)	
						pos_key = 'K' + str(plate_num) + pos 
						hits[pos_key] = [title, total_cells, num_infected, num_uninfected, num_lytic, num_lyso, mode, var, OD] 
	print ' '
	print 'Criteria:' 
	print 'mode=[', mode_lb, mode_ub, ']' 
	print 'n_infected=[', n_infected_lb, n_infected_ub, ']' 
	print 'total_cell=[', n_cell_lb, n_cell_ub, ']'
	print 'frac_infected=[', frac_infected_lb, frac_infected_ub, ']'
	print 'var=[', var_lb, var_ub, ']' 
	print 'n_lytic=[', n_lytic_lb, n_lytic_ub, ']'
	print 'n_lyso=[', n_lyso_lb, n_lyso_ub, ']'
	print 'OD_criteria=[', OD_lb, OD_ub, ']'
	print 'Maynard criteria', in_maynard
	print 'TF criteria', is_TF
	print 'Number of hits meeting criteria: ' + str(counter)
	if save_hits:
		file_name = save_name
		file = open(os.path.join(direc, file_name), 'w')
		json.dump(hits, file)
		file.close()


def print_histogram():
	dataset = load_name_dataset(direc)
	frac_infected_list = []
	mode_list = []
	for name in dataset.keys():
		stats_list = dataset[name]
		total_cells = stats_list[1]
		num_infected = stats_list[2]
		num_uninfected = stats_list[3]
		num_lytic = stats_list[4]
		mode = stats_list[6]
		var = stats_list[7]
		frac_infected = 0
		if num_infected+num_uninfected > 0:
			frac_infected = float(num_infected)/float(total_cells)
		mode_list.append(mode)
		frac_infected_list.append(frac_infected)
	
	plt.figure(0)
	plt.hist(frac_infected_list, 100)
	plt.xlabel('Fraction Infected')
	plt.ylabel('Frequency')
	file_name = 'frac_infected_hist.pdf'
	plt.savefig(os.path.join(direc, file_name), format='pdf')
	plt.close()

	plt.figure(0)
	plt.hist(mode_list, 100)
	plt.xlabel('Inferred Lysis Ratio')
	plt.ylabel('Frequency')
	file_name = 'mode_hist.pdf'
	plt.savefig(os.path.join(direc, file_name), format='pdf')
	plt.close()

	return None

#get_OD_data(plate_numbers = plate_numbers)

#add_plates(direc, plate_numbers)

#compile_dataset(direc, plate_numbers)

#compile_dataset_by_name(direc, plate_numbers)#
