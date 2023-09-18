N, M = map(int, input().split())
lst = []
for i in range(N):
    lst.append(int(input()))
    
lst.sort()
start ,end = lst[0],lst[-1]
mid = (end-start)//2

while lst[0] <= lst[-1]:
    num1 = lst[0] + mid
    num2 = lst[1] + (M-mid)
    if num1 > num2:
        break
    else:
        mid += 1
print(num2)
    
    

