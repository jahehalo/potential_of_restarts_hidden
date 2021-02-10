#!/bin/bash

instances=$(find ../instances -type f -name "*.cnf")
mkdir -p tmp
mkdir -p ../output/probsat_new/times ../output/probsat_new/output
#echo $instances

for instance in ${instances[@]}
do
	f=$(basename $instance)
	python3 main_solver.py -i ${instance} > ../output/probsat_new/times/${f}  2> ../output/probsat_new/output/${f}

done
