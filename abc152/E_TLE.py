# E - Flatten
# https://atcoder.jp/contests/abc152/tasks/abc152_e

from math import *
from collections import defaultdict

MAX_Ai = 10**6
MAX_PRIME = ceil(sqrt(MAX_Ai))
MODE = 10**9+7

N = int(input())
A = map(int, input().split())


def get_prime():
    # prime table
    ptb = [True] * MAX_PRIME
    ptb[0] = ptb[1] = False

    for i in range(2, ceil(sqrt(MAX_PRIME)) + 1):
        for j in range(i*2, MAX_PRIME, i):
            ptb[j] = False

    P = [ i for i, v in enumerate(ptb) if v == True]

    return P

def prime_factorization(n, P):
    factor = defaultdict(int)
    for p in P:
        while n % p == 0:
            factor[p] += 1
            n //= p

    if n != 1:
        factor[n] += 1

    return factor

def main():
    P = get_prime()    

    A_fact = list()
    lcm = defaultdict()
    for a in A:
        a_fact = prime_factorization(a, P)
        A_fact.append(a_fact)
        for prime, power in a_fact.items():
            if prime not in lcm:
                lcm[prime] = power
            else:
                if lcm[prime] < power:
                    lcm[prime] = power

    ret = 0
    for a_fact in A_fact:
        b_fact = {key: lcm[key] - a_fact.get(key, 0) for key in lcm.keys()}
        tmp = 1
        for prime, power in b_fact.items():
            tmp *= prime**power
        ret += tmp

    print(ret%MODE)


if __name__ == "__main__":
    main()
