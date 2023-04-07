N = int(input())
lst = []
room = []

for i in range(N):
    start ,end = map(int,input().split())
    lst.append([start,end])

lst.sort(key = lambda x:x[0])

room.append(lst[0][1])

for i in range(1, N):
    cnt  = 0 
    for j in range(len(room)):
        if room[j] > lst[i][0]:
            room.append(lst[i][1])
        else:
            room[j] = lst[i][1]
            cnt += 1
    if cnt == 1:
        room.pop(lst[i][1])
        
print(len(room))
            
            
