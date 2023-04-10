N, M = map(int, input().split())


cur_lst = [list(map(int,list(input()))) for _ in range(N)]
last_lst = [list(map(int,list(input()))) for _ in range(N)]

cnt = 0

def change(x,y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            cur_lst[i][j] = 1 - cur_lst[i][j]
            
for i in range(N - 2):
    for j in range(M - 2):
        if cur_lst[i][j] != last_lst[i][j]:
            change(i,j)
            cnt += 1
    
    
if cur_lst != last_lst:
    print("-1")
else:
    print(cnt)
        


