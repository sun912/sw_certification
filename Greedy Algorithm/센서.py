from sys import stdin
readl = stdin.readline


def sol(n, k, positions):
    gap = []
    positions.sort()
    current = positions[0]
    for i in range(1, len(positions)):
        gap.append(positions[i] - current)
        current = positions[i]

    gap.sort()
    return sum(gap[0:n-k])


if __name__ == "__main__":
    n = int(readl())
    k = int(readl())
    positions = list(map(int, readl().split()))
    print(sol(n, k, positions))
