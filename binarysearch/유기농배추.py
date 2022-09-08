# https://www.acmicpc.net/problem/1012
from collections import deque
from sys import stdin

readl = stdin.readline

case_number = int(readl().rstrip())

sol = []
for _ in range(case_number):
    count = 0
    w, h, k = list(map(int, readl().split()))
    p = [list(map(int, readl().split())) for _ in range(k)]

    array = [[0]*h for _ in range(w)]

    for x, y in p:
        array[x][y] = 1

    visited = [[False]*h for _ in range(w)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(w):
        for j in range(h):

            if array[i][j] == 1 and visited[i][j] is False:
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                while q:
                    x, y = q.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < w and 0 <= ny < h and visited[nx][ny] is False and array[nx][ny] == 1:
                            q.append((nx, ny))
                            visited[nx][ny] = True
                        else:
                            continue
                count += 1

    sol.append(count)

print(*sol, sep='\n')
