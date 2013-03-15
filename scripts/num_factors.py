import multiprocessing
import os
import sys

from collections import defaultdict
from collections import Counter
from datetime import datetime
from IPython.parallel import Client

# The script should print a dictionary.
# This script should take an argument which is a character controlling how the script will run.
# Remember to start the cluster before running the script.
if len(sys.argv) != 2:
    print("You should give one argument which should be a character, s, m or i, which will determine how the script will run. Serially (s), with multiprocessing (m) or with IPython parallel (i).")
    sys.exit()
control_char = sys.argv[1]

integers = range(2, 500001)
# Testing
#integers = range(2, 11)

def factorize(n):
    if n < 2:
        return []
    factors = []
    p = 2

    while True:
        if n == 1:
            return factors
        r = n % p
        if r == 0:
            factors.append(p)
            n = n / p
        elif p * p >= n:
            factors.append(n)
            return factors
        elif p > 2:
            p += 2
        else:
            p += 1
try:
    cli = Client()
except IOError:
    print("Start the IPython cluster before running this script! Use for example: \"ipcluster start -n 4\"")
    sys.exit()
dview = cli[:]
dview["factorize"] = factorize

def task_serial(args):
    factors = (factorize(args))
    return os.getpid(), args, factors

def task_multip(args):
    factors = factorize(args)
    return os.getpid(), args, factors

@dview.parallel(block=True)
def task_ipy_par(args):
    import os
    factors = factorize(args)
    return os.getpid(), args, factors

def histogram_func(results):
    histogram = defaultdict(int)
    for result in results:
        factors = result[2]
        count = Counter(factors)
        unique_count = len(count)
        histogram[unique_count] += 1
    print(histogram)
    print("Execution time: "+str(datetime.now()-start_time))
    return None

start_time = datetime.now()

if control_char == "s":
    results = map(task_serial, integers)
    histogram_func(results)
elif control_char == "m":
    if __name__ == "__main__":
        pool = multiprocessing.Pool(processes=(multiprocessing.cpu_count()-1))
        r = pool.map_async(task_multip, integers)
        results = r.get()
        histogram_func(results)
elif control_char == "i":
    results = task_ipy_par.map(integers)
    histogram_func(results)
else:
    print("You should give one argument which should be a character, s, m or i, which will determine how the script will run. Serially (s), with multiprocessing (m) or with IPython parallel (i).")
    sys.exit()
