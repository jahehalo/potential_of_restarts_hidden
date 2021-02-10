import numpy as np 
import pandas as pd 

import os


base_path = f"../../sputnik/sputnik_client/output_train/"
data_list = []
names = []
for instance_type in os.listdir(base_path):
	type_path = base_path + instance_type + "/"
	for size in os.listdir(type_path):
		size_path = type_path + size + "/"
		for instance in os.listdir(size_path):
			try:
				data = np.loadtxt(size_path + instance, usecols=0)
			except ValueError:
				print(f"skipped instance {instance}")
				continue
			data = np.sort(data)
			data_list.append( [] + [instance_type] + list(data) )
			names.append(instance)

print(data_list)
df = pd.DataFrame(data_list, index=names)
df.to_csv("./all_data.csv")