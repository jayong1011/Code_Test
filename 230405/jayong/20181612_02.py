N , K = map(int, input().split())

if N == 1:
    cnt = 1
else:
    cnt = 0

def sosu(N):
    cnt = 0
    for i in range(1,N):
        if N % i == 0:
            cnt += 1
    if cnt == 1:
        return N
                 


while N <= K:
    num = sosu(N)
    if num:
        part_sosu = num*num
        if part_sosu <= K:
            cnt += 1
    N += 1 
print(cnt)        