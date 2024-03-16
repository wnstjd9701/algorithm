# 1226. [S/W 문제해결 기본] 7일차 - 미로1
from collections import deque

dx, dy = [0,0,-1,1], [1,-1,0,0]
def bfs(x, y, end_x, end_y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == end_x and y == end_y:
            return 1            

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<16 and 0<=ny<16 and not visited[nx][ny] and graph[nx][ny] != 1:
                visited[nx][ny] = 1
                q.append((nx, ny))
    return 0
T = 10
for _ in range(1, T+1):
    tc = int(input())
    graph = [list(map(int, input())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]

    start_x, start_y = 0, 0
    end_x, end_y = 0, 0

    for i in range(16):
        for j in range(16):
            if graph[i][j] == 2:
                start_x = i
                start_y = j
            elif graph[i][j] == 3:
                end_x = i
                end_y = j
    answer = bfs(start_x, start_y, end_x, end_y)
    print("#{} {}".format(tc, answer))