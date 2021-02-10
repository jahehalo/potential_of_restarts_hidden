import os
import pandas as pd

base_path = './mlp_agressive'
results_path = os.path.join(base_path, 'results')
times_path = os.path.join(results_path, 'times')


files = []
types = []
times = []
for file in os.listdir(times_path):
	if 'fla' in file:
		if 'komb' in file:
			file_type = 'komb'
		elif 'qhid' in file:
			file_type = 'qhid'
		else:
			file_type = 'barthel'
	else:
		if 'p12' in file:
			file_type = 'unif_medium'
		else:
			file_type = 'unif_huge'

	file_path = os.path.join(times_path, file)
	with open(file_path, 'r') as f:
		time = f.readline()
		time = float(time)
		if time == 5000.0:
			time = 10000
	
	files.append(file)
	types.append(file_type)
	times.append(time)


df = pd.DataFrame(data={'type':types, 'times':times}, index=files)
df.to_csv(os.path.join(results_path, 'results.csv'))