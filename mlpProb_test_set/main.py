import argparse
from subprocess import Popen, PIPE
import sys
from timeit import default_timer as timer

import numpy as np
import pandas as pd
from joblib import load

from expon_mixture import ExponMixture


def run_alg(instance, t, seed):
    p = Popen(['./probSAT', f"-m {t}", instance, str(abs(seed))], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    rc = p.returncode
    err = err.decode("utf-8")
    if err != "":
        print(err, file=sys.stderr)
    return output
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--seed", type=int, default=1909, help="The seed.")
    parser.add_argument("-i", "--instance", default='./instances/uf250-01.cnf', help="The instance.")

    args = parser.parse_args()

    regr_rf = load('rf_agressive.joblib')
    df = pd.read_csv('./test_features.csv')
    df.set_index('instance', inplace=True)
    data = np.asarray(df.loc[args.instance.replace("./","").replace("cnfs/", "")], dtype=np.float)
    y = regr_rf.predict(data.reshape((1, len(data))))[0]
    t = np.ceil(ExponMixture([y[0], 1-y[0]], [y[1], y[2]]).find_restart_time(n=data[0]))

    start = timer()
    flips = run_alg(args.instance, int(t), args.seed)
    end = timer()
    
    flips = flips.decode("utf-8")
    flips = flips.replace(" 1\n", "").rstrip()
    print(flips, end-start, str(abs(args.seed)))


    
    

    
