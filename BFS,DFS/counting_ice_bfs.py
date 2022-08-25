from collections import deque

# bfs로 구멍이 뚫린곳을 확인하고 1이 나오면 카운트 + 1


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    if input_list[x][y] == 1:
        return False

    while queue:
        x, y = queue.popleft()
        input_list[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and input_list[nx][ny] == 0:
                queue.append((nx, ny))

    return True


ice_count = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())

input_list = [list(map(int, input())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if bfs(i, j) == True:
            ice_count += 1

print(ice_count)
