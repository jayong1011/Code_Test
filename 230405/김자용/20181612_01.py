N, K = map(int,input().split())
lst = []
sosu_lst = []
print(N, K)


for i in range(2, N+1):
    lst.append(i)
    
for i in lst:
    print(i)
    count = 0
    for j in range(1,i):
        if i % j == 0:
            count += 1
    if count == 1:
         sosu_lst.append(i)

for i in sosu_lst:
    P = min(sosu_lst)
    sosu_lst.pop(P)
    print(sosu_lst)