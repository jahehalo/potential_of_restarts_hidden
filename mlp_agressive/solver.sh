#!/bin/bash

instance=$1

def_line=$(grep -m 1 "^p" ${instance})
n_vars=$(echo ${def_line} | egrep -o "cnf [[:digit:]]*" | egrep -o "[[:digit:]]*")
m_clauses=$(echo ${def_line} | egrep -o "[[:digit:]]*$")

if [ $n_vars -gt 1000 ]
then
	./probSAT -a ${instance} 10 
else
	k=$(( m_clauses/n_vars ))
	if [ $k -gt 6 ]
	then
		./probSAT -a ${instance} 10
	else
		output=$(./probSAT -m 1000000 -t 1 -a ${instance} 10)
		rc=$?
		if [ $rc -eq 10 ] # probSAT found a solution
		then
			echo "${output}"
			exit 10
		fi
		restart=$(python3 predict_restart.py -i ${instance})
		./probSAT -m ${restart} -a ${instance} 11
	fi
fi
