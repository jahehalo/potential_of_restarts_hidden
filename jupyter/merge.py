import os
from glob import glob
from collections import defaultdict

def filter_file(file, type_size):
	with open(file, 'r') as f:
		lines = f.readlines()
	result = []
	for line in lines:
		prefix, *_ = line.split(" ")
		suffix = prefix.split(".cnf")[1]
		line = line.replace(suffix, "")
		line = type_size + line
		line = line.replace(" ", ",")
		result.append(line)
	return result

folders = ['barthel', 'komb', 'qhid']

fit_dict = defaultdict(list)
for folder in folders:
	files = glob(f"{folder}/**/*fits.txt")
	for file in files:
		type_size = file.rsplit("/", maxsplit=1)[0] + "/"
		fits = filter_file(file, type_size)
		fit_type = file.split("/")[-1]
		fit_dict[fit_type].extend(fits)

for fit_type in fit_dict:
	fits = fit_dict[fit_type]
	with open(fit_type, 'w') as f:
		try:
			f.write(''.join(fits))
		except TypeError:
			print(f"Failed on type {fit_type} with list {fits}")
			quit()