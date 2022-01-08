from colorama import Fore, Style
from cases import nMiss, Rieman
from pprint import pprint
import argparse, sys
import math


# Calculates the Riemann-Zeta zeroes
def riemann(n):
    n_zeros = str(2*(n +1))
    print(f"For {str(n)} we have {n_zeros} zeros")
    firsthalf = [] 
    secondhalf = []    

    x = list(range(0,n + 1))
    theta = math.pi/3
    for i in x:
        y = (math.pi/3)*(1+6*i)
        y = math.sqrt((y**2/theta**2)-0.25)
        firsthalf.append({i : y}) #"The first half of zeros"
        z = (5*math.pi/3)*(1+6/5*i)
        z = math.sqrt((z**2/theta**2)-0.25)
        secondhalf.append({i : z}) #"The second half of zeros"
        # print(results)
        


    return Rieman(n, n_zeros, firsthalf, secondhalf).__dict__

# Calculates Fermat near-misses for a given range for the base and given n
def getFermatMiss(a,b,c, n):
    
    # c = math.pow(math.pow(a, n) + math.pow(b, n), n)
    # print(c)
    d = (math.pow(c, n) - math.pow(a, n) - math.pow(b, n))
    nr = (n*math.pow(c, n-3))
    # print(f"{math.pow(c, n)}-{math.pow(a, n)}-{math.pow(b, n)} = {d} c-{math.pow(c, n-3)}")
    if d == 0:
        d = 1
    nm = round(nr/d, 1)
    return nMiss(a,b,c,nm).__dict__


def main():
    parser = argparse.ArgumentParser(description="Calculater Fermat near-misses and Riemann-Zeta zeroes.")
    parser.add_argument("-f", "--fermat", help="Calculate Fermat near-misses", action='store_true')
    parser.add_argument("-r", "--rieman", help="Calculate Riemann-Zeta zeroes", action="store_true")
    parser.add_argument("-n", help = "value of n")


    
    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()

    if not args.n:
        n = int(input("Please enter value for n(>2) :"))
    else:
        try:
            n = int(args.n)
        except ValueError:
            print(f"[!]{Fore.RED}Please re-run with a valid value of n")
            sys.exit(1)





    if n < 2:
        print(f"[!]{Fore.RED}Value of n should be > 2")
        sys.exit(1)

    if args.fermat:
        print(f"\n{Fore.BLUE}\tFermat near-misses {Style.RESET_ALL} when start n = {n}")
        a = int(input("Enter a (a > 0)      : "))
        b = int(input("Enter b (b >= a)     : "))
        c = int(input("Enter c (b < c < 2^23 ) : "))

        # start = int(input("Enter start number :"))
        if not 0 < a <= b < c < 2**23:
            print("Enter valid range a,b or c")
            sys.exit(1)
        # for i in range(n, (n*4)):  
        pprint(getFermatMiss(a, b,c, n))
    if args.rieman:
        print(f"\n{Fore.BLUE}\tRiemann-Zeta zeroes {Style.RESET_ALL} when n = {n}")
        pprint(riemann(n))
        print("\n")



if __name__ == "__main__":
    main()

