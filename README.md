These folders contain supplementary data to "The Potential of Restarts for ProbSAT" on hidden instances 
by Jan-Hendrik Lorenz. Ulm University 
Institute of Theoretical Computer Science


The instances from the training and test set are located in the "instances" folder. The results on these instances (measured in flips) are placed in the "outputs" folder. The subfolders "output_train" and "output_test" are for probSAT without restarts, while the results of the mlpProb strategy on the test set are in the subfolder "output_test_agressive". The subfolder "output_test_restart" contains the results of another restart strategy that was discarded later on. For the results with restarts on the test set, the code in the "mlpProb_test_set" folder was used.
The results on the training and test set are evaluated in the "jupyter" folder. The exponential mixture distributions are also fitted there, and the random forest is trained.


The code and random forest for the final mlpProb strategy are located in "mlp_agressive" whereas the folder "mlp_cautious" describes a different restart strategy that uses somewhat more conservative restart times. The latter restart strategy is described in more detail in the dissertation since the aggressive strategy is almost always better. The latter restart strategy is not described in detail in the thesis since the aggressive strategy is almost always better.
The folder "SAT_competition18_results" includes the results on the instances and under the conditions of the SAT competition 2018. It compares the results of mlpProb (see "mlp_agressive"), the conservative strategy (see "mlp_cautious") with the original version of probSAT as well as sparrow2Riss and gluHack. The latter two won the first two places each at the SAT Competition 2018.


The instances of SAT Competition 2018 are available at the following link: http://sat2018.forsyte.tuwien.ac.at/benchmarks/Random.zip.
In order to execute the "mlp_agressive" and the "mlp_cautious" strategy, the featureSAT12 program must also be compiled and placed in those directories. The source code for this program can be downloaded from http://www.cs.ubc.ca/labs/beta/Projects/SATzilla/. In addition, probSAT, which can be found in the directory "probSAT_dir", has to be compiled and placed in the respective folders.
One can then start the pipeline restart strategy by executing main_solver.py.
