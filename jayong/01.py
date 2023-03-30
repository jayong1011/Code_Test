N = int(input())
A = list(map(int,input().split()))
S = int(input())
count = 0
assert len(A) == N

for i in range(0,len(A),2):
    if A[i] < A[i+1]:
        index = A[i+1]
        A[i+1] = A[i]
        A[i] = index
        count += 1
    if count == S:
        break
    
print(A)
    
    