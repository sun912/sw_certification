from collections import deque


def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque()
    q.append((x, y))
    value = []
    while q:
        x, y = q.popleft()
        if input_data[x][y] > 0:

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and input_data[nx][ny] == 1:
                    input_data[nx][ny] += input_data[x][y]
                    q.append((nx, ny))
    return input_data[n-1][m-1]


n, m = map(int, input().split())
input_data = [list(map(int, input())) for _ in range(n)]

print(bfs(0, 0))
# print(min(result))
