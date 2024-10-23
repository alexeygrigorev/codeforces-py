# https://codeforces.com/contest/2025/problem/B

import sys


def solve(input_source=sys.stdin):
    input_source.readline() # skip k
    input_source.readline() # skip n

    ks = list(map(int, input_source.readline().split()))

    max_k = max(ks)

    powers = [1] * (max_k + 1)

    for i in range(1, max_k + 1):
        powers[i] = (powers[i - 1] * 2) % 1_000_000_007
    
    for k in ks:
        print(powers[k])



if __name__ == "__main__":
    solve()