"""
5

2 3
11      2233 = 11 * 203

0 1
2       10 = 2 * 5

4 3 2 1
5       Impossible

0
10      Impossible

9
9       9 = 9 * 1

"""



"""
-sort lucky nums ie 1,2,3,4 (form 4,3,2,1 or similar)
-sift trough permutations, dividing by x, 1234,1243,...4312,4321
-no answer, add lowest, permutate, 11234,11243,...43121,43211
-next probably gonna be 12234,12334,12344, then 112234, this could get messy
"""
#impossible if: x is 5 and 0 or 5 not in luckynums
#               x is odd and luckynums are all even
#               x is even and luckynums are all odd
#               luckynums is only 0 (apparently x*0 isn't valid per example)

from itertools import permutations

def find_y(luckynums):
    luckynums = sorted(luckynums)
    x = int(raw_input('> '))
    lnlen = len(luckynums)
    if (lnlen == 1 and luckynums[0] == 0) or (
            x==5 and 5 not in luckynums) or (
            x==5 and 0 not in luckynums) or (
            x%2==0 and all(l%2==1 for l in luckynums)) or (
            x%1==1 and all(l%2==0 for l in luckynums)) or (
            #sum([z if z != 1 else 0 for z in luckynums])%3==0 and 
            #sum([int(y) for y in str(x)])%3!=0) or (
            #sum([z if z != 1 else 0 for z in luckynums])%3!=0 and 
            #sum([int(y) for y in str(x)])%3==0
            ):
        return "Impossible"
    luckynums = map(str, luckynums)
    if lnlen == 1:
        lnum = luckynums[0]
        luckynums=luckynums[0]
        while True:
            currentperm = int(luckynums)
            if currentperm%x==0:
                return "%d = %d * %d"%(currentperm, x, currentperm/x)
            luckynums=luckynums+lnum
            
            
    lnums=luckynums[:]
    currentperm = int(''.join(luckynums))
    gap = 1
    i,j = 0,gap
    mults = 1
    while True:
        for perm in permutations(luckynums, lnlen):
            currentperm = int(''.join(perm))
            if currentperm%x==0:
                return "%d = %d * %d"%(currentperm, x, currentperm/x)
        luckynums = sorted(lnums+(lnums[i:j]*mults))
        lnlen = len(luckynums)
        i+=1
        j=i+gap
        if j > lnlen:
            gap+=1
            i=0
            j=i+gap
        if gap>lnlen:
            mults+=1
            luckynums = sorted(lnums[:])
            gap=1
            i=0
            j=i+gap
            
        #print luckynums, gap, i, j
    return "Impossible"

def lmod():
    for tc in xrange(int(raw_input('> '))):
        print find_y(map(int,raw_input('> ').split()))

if __name__ == "__main__":
    for tc in xrange(int(raw_input('> '))):
        print find_y(map(int,raw_input('> ').split()))
