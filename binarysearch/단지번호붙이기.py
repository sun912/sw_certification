from collections import deque
from sys import stdin
readl = stdin.readline

n = int(readl())

array = [list(map(int, readl().rstrip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
q = deque()


def bfs(x, y):
    q.append((x, y))
    count = 0

    while q:
        x, y = q.popleft()
        count += 1

        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] == True or array[nx][ny] == 0:
                continue
            else:
                q.append((nx, ny))
                visited[nx][ny] = True
    return count


result = []

for i in range(n):
    for j in range(n):
        if array[i][j] == 1 and visited[i][j] == False:
            visited[i][j] = True
            result.append(bfs(i, j))

result.sort()
print(len(result))
print(*result, sep='\n')
