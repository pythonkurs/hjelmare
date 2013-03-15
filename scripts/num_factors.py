import sys

from collections import defaultdict
from collections import Counter

#The script should print a dictionary
#This script should take an argument which is a character.
if len(sys.argv) != 2:
    print("You should give one argument which should be a character, s, m or i, which will determine how the script will run. Serially (s), with multiprocessing (m) or with IPython parallel (i).")
    sys.exit()
control_char = sys.argv[1]

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

histogram = defaultdict(int)

integers = range(2, 500001)
# Testing
#integers = range(2, 11)

if control_char == "s":
    for integer in integers:
        factors = (factorize(integer))
        count = Counter(factors)
        unique_count = len(count)
        #print(factors)
        #print(unique_count)
        histogram[unique_count] += 1
    print(histogram)
else:
    print("You should give one argument which should be a character, s, m or i, which will determine how the script will run. Serially (s), with multiprocessing (m) or with IPython parallel (i).")
    sys.exit()


#if control_char == "m":



#if control_char == "i":

