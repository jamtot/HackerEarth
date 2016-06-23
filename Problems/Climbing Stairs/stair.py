def bruteloop(): # too slow
    ABN=map(int,raw_input().split())
    A,B,N=ABN[0],ABN[1],ABN[2]
    cur=0
    if A>=N: 
        return 1
    else:
        days=1
        while cur<N:
            cur+=A  
            if cur>=N:
                return days
            cur-=B
            days+=1

import math

def days():
    ABN=map(int,raw_input().split())
    A,B,N=ABN[0],ABN[1],ABN[2]
    if A>=N: return 1
    else:
        return int(math.ceil(1.0*(N-B)/(A-B)))

if __name__ == "__main__":
    print days()
