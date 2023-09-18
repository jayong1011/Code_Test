t = int(input())
lst = []
dp = [[1 for _ in range(31)] for _ in range(31)]


for i in range(1, 31):
    for j in range(i, 31):
        dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
    
    
for i in range(t):
    N, M = map(int, input().split())
    assert 0 < N <= M < 30
    lst.append(dp[N][M-1])


for i in range(len(lst)):
    print(lst[i])