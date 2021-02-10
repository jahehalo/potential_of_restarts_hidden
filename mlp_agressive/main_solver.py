import argparse
from subprocess import Popen, PIPE, TimeoutExpired
from sys import stderr
from time import perf_counter
from os import setsid, killpg
from signal import SIGTERM

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--instance", default='./instances/uf250-01.cnf', help="The instance.")
    args = parser.parse_args()

    t_out = 5000

    t = perf_counter()
    p = Popen(['numactl', '--cpunodebind=1', './solver.sh', args.instance],stdin = PIPE, stdout = PIPE, stderr=PIPE, preexec_fn=setsid)
    try:
        output, err = p.communicate(timeout=t_out)
        t = perf_counter() - t
        rc = p.returncode
        print(err.decode("utf-8"), output.decode("utf-8"), file=stderr)
    except TimeoutExpired:
        t = t_out
        killpg(p.pid, SIGTERM)
        output, err = p.communicate()

    print(t)
