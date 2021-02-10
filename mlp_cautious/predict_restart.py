import argparse
from subprocess import Popen, PIPE

import numpy as np
from joblib import load

from expon_mixture import ExponMixture



parser = argparse.ArgumentParser()
parser.add_argument("-i", "--instance", default='./instances/uf250-01.cnf', help="The instance.")
args = parser.parse_args()

p = Popen(['./featuresSAT12', "-base", "-ls", "-lobjois", args.instance], stdin=PIPE, stdout=PIPE, stderr=PIPE)
regr_rf = load('rf_regressor.joblib')
data, _ = p.communicate()
data = np.asarray(data.decode("utf-8").split("\n")[-2].split(","), dtype=np.float)
y = regr_rf.predict(data.reshape((1, len(data))))[0]
print(int(ExponMixture([y[0], 1-y[0]], [y[1], y[2]]).find_restart_time(n=data[0])))



    
    

    
