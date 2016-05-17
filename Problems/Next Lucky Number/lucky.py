def next_lucky(n):
    if len(n) == 0:
        return ''
    if int(n[0]) < 3:
        return '3'*len(n)
    elif int(n[0]) == 3:
        pos1 = int(n[0]+next_lucky(n[1:]))
        pos2 = int('5'+'3'*(len(n)-1))
        if pos1 > pos2: pos1,pos2 = pos2,pos1
        if pos1 > int(n):
            return str(pos1)
        else:
            return str(pos2)
    elif int(n[0]) < 5:
        return '5'+'3'*(len(n)-1)
    elif int(n[0]) == 5:
        pos1 = int(n[0]+next_lucky(n[1:]))
        pos2 = int('3'*(len(n)+1))
        if pos1 > pos2: pos1,pos2 = pos2,pos1
        if pos1 > int(n):
            return str(pos1)
        else:
            return str(pos2)
    elif int(n[0]) > 5:
        return '3'*(len(n)+1)


if __name__ == "__main__":
    assert next_lucky('33')=='35'
    assert next_lucky('35')=='53'
    assert next_lucky('200')=='333'
    assert next_lucky('5555')=='33333'

    for testcase in xrange(int(raw_input())):
        print next_lucky(raw_input())

#----------original attempt----------
# brute force, too slow
"""
import re

def next_lucky(n):
    n+=1
    nstr = str(n)
    nlen = len(nstr)
    while re.search(r'[^35]', nstr):
        n+=1
        nstr=str(n)
    return n
        

if __name__ == "__main__":
    for testcase in xrange(int(raw_input())):
        print next_lucky(int(raw_input()))
"""
