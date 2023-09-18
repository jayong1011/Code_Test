N,C = map(int, input().split())
lst = []
for i in range(N):
    lst.append(int(input()))
    
start, end = 1, max(lst)
lst.sort()


def get(start, end):
    global answer 
    while start <= end:
        mid = (start+end) // 2
        cnt = 1
        cur = lst[0]
        for i in range(1, len(lst)):
            if lst[i] >= cur + mid:
                cnt += 1
                cur = lst[i] 
        if cnt >= C:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
            
get(start, end)
print(answer)
            
    