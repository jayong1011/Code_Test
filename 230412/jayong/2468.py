N = int(input())

lst = [list(map(int, input().split())) for _ in range (N)]

sum = []
print(lst)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[False] * N for _ in range (N)]
print(visited)

def ans(x,y):
    if x >= 0 or y >= 0  or x < N or y < N:
        if lst[x][y] > N and visited[x][y] == False:
            visited[x][y] = True
            global cnt
            cnt += 1
            ans(x,y+dy[0])
            ans(x,y+dy[1])
            ans(x+dx[2],y)
            ans(x+dx[3],y)
            
            
cnt = 0 
    
for i in range(N):
    for j in range(N):
        print(i,j)
        ans(i,j)
        sum.append(cnt)
print(sum)
        
    
         