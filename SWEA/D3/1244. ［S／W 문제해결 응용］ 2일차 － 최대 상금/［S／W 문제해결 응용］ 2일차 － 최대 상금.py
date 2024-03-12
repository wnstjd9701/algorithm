# 1244. [S/W 문제해결 응용] 2일차 - 최대 상금 
def dfs(n):
    global result
    if n == N:
        result = max(result, int("".join(map(str, num))))
        return 
    for i in range(L-1):
        for j in range(i+1, L):
            num[i], num[j] = num[j], num[i]

            check = int("".join(map(str, num)))
            if (n, check) not in visited:
                dfs(n+1)
                visited.append((n, check))

            num[j], num[i] = num[i], num[j]

T = int(input())

for test_case in range(1, T + 1):
    st, t = map(str, input().split())
    num, visited = [], []
    N = int(t)
    L = len(st)
    result = 0

    for i in st:
        num.append(i)
    dfs(0)
    print("#{} {}".format(test_case, result))
