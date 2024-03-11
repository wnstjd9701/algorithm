# 백준 14502번 문제 - 연구소
from collections import deque
import copy
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
dx, dy = [0,0,-1,1], [1,-1,0,0]
for _ in range(n):
    graph.append(list(map(int, input().split())))
def bfs():
    queue = deque()
    temp_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if temp_graph[i][j] == 2:
                queue.append((i,j))
    while queue:
        x, y = queue.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if temp_graph[nx][ny] == 0:
                temp_graph[nx][ny] = 2
                queue.append((nx,ny))
    cnt = 0
    global answer
    for i in range(n):
        cnt += temp_graph[i].count(0)

    answer = max(answer, cnt)

def makeWall(cnt,x,y):
    if cnt == 3:
        bfs()
        return
    # 시간초과를 방지하기 위해 
    # 이전 재귀에서 탐색한 범위를 제외하고 for문 수행
    for i in range(x, n):
        if i == x:
            k = y
        else:
            k = 0
        for j in range(k, m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt+1,i,j)
                graph[i][j] = 0
answer = 0 
makeWall(0,0,0)
print(answer)