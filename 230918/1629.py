import sys
input = sys.stdin.readline

A,B,C = map(int, input().split())


def gob(A,B):
    if B == 1:
        return A % C
    else:
        tmp = gob(A, B//2)
        if B % 2 == 0:
            return (tmp * tmp) % C
        else:
            return(tmp * tmp * A) % C
            