import math
import sys
from decimal import *

def max(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return a

def factorial(x):
       if x==0:
           return 1
       else:
           return Decimal(x*factorial(x-1))

lastCalc = Decimal(0)
def main():
    global lastCalc

    sum = Decimal(0)
    n = Decimal(0)
    i = Decimal((math.sqrt(8))/9801)

    while True:
        #Ramanujan's Formula:-
        frac1Num = Decimal(i*(factorial(4*n)))
        frac1Den = Decimal(pow(factorial(n),4))
        frac1 = frac1Num/frac1Den
        frac2 = Decimal(((26390*n+1103)/pow(396,4*n)))
        tmp = frac1 * frac2
        sum +=tmp
        
        n += 1
        pi = 1/sum
        print(pi)
        if pi == lastCalc:
            f = open("pi.txt", "w")
            f.write(str(pi))
            f.close()
            break

        lastCalc = pi

desiredSpecificity = int(sys.argv[1])
getcontext().prec = desiredSpecificity
sys.setrecursionlimit(max(math.floor(desiredSpecificity/1.5), 1000))
main()