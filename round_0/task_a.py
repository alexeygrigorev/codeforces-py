import sys

def solve(input_source=sys.stdin):
    n = int(input_source.readline().strip())
    values = list(map(int, input_source.readline().split()))
    result = sum(values)
    print(result)

if __name__ == "__main__":
    solve()