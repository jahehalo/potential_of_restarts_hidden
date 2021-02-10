#!/bin/bash

instances=$(find ../instances -type f -name "*.cnf")
mkdir -p tmp
mkdir -p ../output/mlp_agressive/times ../output/mlp_agressive/output
#echo $instances

for instance in ${instances[@]}
do
	f=$(basename $instance)
	if [[ $f == *"fla"* ]]; then
		python3 main_solver.py -i ${instance} > ../output/mlp_agressive/times/${f}  2> ../output/mlp_agressive/output/${f}
	fi

done
