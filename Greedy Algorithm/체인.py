import sys

readl = sys.stdin.readline


def solution(n, chains):
    count = 0
    chains.sort()
    current = 0

    for chain in chains:
        if chain == n - 1:
            return current + chain
        elif chain > n - 1:
            return current + n-1
        else:
            n -= (chain + 1)
            current += chain

    return count


if __name__ == "__main__":
    n = int(readl())
    chains = list(map(int, input().split()))
    print(solution(n, chains))
