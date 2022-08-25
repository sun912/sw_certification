gridmap = [list(map(int, input())) for _ in range(4)]
count = 0


def dfs(x, y):
    if x < 0 or x >= 4 or y < 0 or y >= 5:
        return False

    if gridmap[x][y] == 1:
        gridmap[x][y] = 0

        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True

    return False


for i in range(4):
    for j in range(5):
        if dfs(i, j):
            count += 1
print(count)
