#백준_1083번_송가은
print("")

n = int(input())
a = list(map(int, input().split()))
s = int(input())


for i in range(n):
    end = 0
    end = i+s+1
    if n > end:
        max_idx = a.index(max(a[i:end]))
    elif n <= end:
        max_idx = a.index(max(a[i:n]))
    for j in range(max_idx, i,-1):
        a[j-1] ,a[j] = a[j], a[j-1]
        s = s-1
        if s == 0:
            break
    if s == 0:
        break

print(*a)


#stop = 0

#for i in range(1,N):
#  if A[i-1] < A[i]:
#    temp = A[i-1]
#    A[i-1] = A[i]
#    A[i] = temp
#    stop = stop +1
  
#  if stop == S:
#    break

#for i in A:
#  print(i, end=' ')

        

#for i in range(1,N):
#  if A[i-1] < A[i]:
#    temp = A[i-1]
#    A[i-1] = A[i]
#    A[i] = temp
#    stop = stop +1
  
#  if stop == S:
#    break

#for i in A:
#  print(i, end=' ')