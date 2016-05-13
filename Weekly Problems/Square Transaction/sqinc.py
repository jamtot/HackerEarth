from collections import defaultdict

def sqinc():
    t = int(raw_input())
    costs = reduce(lambda l, v: (l.append(l[-1] + v) or l), map(int, raw_input().split()), [0])[1:]
    trandict = defaultdict(lambda: -1)
    j=0
    for i in xrange(1, costs[-1]+1):
        if i > costs[j]:
            j+=1
        trandict[i]=j+1
    q = int(raw_input())
    for i in xrange(q):
        print trandict[int(raw_input())]

if __name__ == "__main__":
    sqinc()

#-Previous submissions-------------

# too slow to complete the largest input in under 5 seconds

""" 
def sqinc():
    t = int(raw_input())
    transactions = map(int, raw_input().split())
    costs = [sum(transactions[:i+1]) for i in xrange(t)]
    trandict = defaultdict(lambda: -1)
    j=0
    for i in xrange(1, costs[-1]+1):
        if i > costs[j]:
            j+=1
        trandict[i]=j+1
    q = int(raw_input())
    for i in xrange(q):
        print trandict[int(raw_input())]
"""

"""
def sqinc():
    t = int(raw_input())
    transactions = map(int, raw_input().split())
    costs = [sum(transactions[:i+1]) for i in xrange(t)]
    q = int(raw_input())
    targets = [int(raw_input()) for i in xrange(q)]
 
    for target in targets:
        if target > costs[-1]: print -1
        else:
            for i in xrange(t):
                if costs[i] >= target:
                    print i+1
                    break
            else:
                print -1
"""

"""
def sqinc():
    t = int(raw_input())
    transactions = map(int, raw_input().split())
    q = int(raw_input())
    for i in xrange(q):
        target = int(raw_input())
        achieved = 0
        for j in xrange(len(transactions)):
            achieved+=transactions[j]
            if achieved >= target:
                print j+1
                break
        else:
            print -1
"""
