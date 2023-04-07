def asn(A,B, cnt):
    
    if B % 10 == 1:
        cnt += 1
        B -= 1
        B //= 10
        temp = B
        
    elif B % 2 == 0:
        cnt += 1
        B //= 2
        temp = B
        
    if A > temp:
        print("-1")
        return 
    elif A == temp:
        print(cnt)
        
        return
        
    asn(A,B,cnt)


A , B = map(int, input().split())
cnt = 1
asn(A, B, cnt)