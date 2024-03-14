# 1210. [S/W 문제해결 기본] 2일차 - Ladder1 [D4]
for _ in range(1, 11):
    tc = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]
    visited = [[0]*100 for _ in range(100)]

    start = graph[99].index(2)
    x, y = 99, start

    while x != 0:
        visited[x][y] = 1
        if y - 1 >= 0 and graph[x][y-1] and visited[x][y-1] == 0:
            y -= 1
            continue
        elif y + 1 < 100 and graph[x][y+1] and visited[x][y+1] == 0:
            y += 1
            continue
        else:
            x -= 1
    
    answer = y
    print("#{} {}".format(tc, answer))