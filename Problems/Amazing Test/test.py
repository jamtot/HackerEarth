def findSum(anslist, target, L, combo=[]):
    if anslist:
        return
    if not target:
        anslist.append(combo)
        return
    if target < 0:
        return
    for i in xrange(len(L)):
        findSum(anslist, target-L[i], L[:i]+L[i+1:], combo+[L[i]])

def amazing_test():
    N, X = map(int, raw_input().split())
    # the reverse sort sped up the processing of longer testcases
    # by a lot, bringing the overall test input from 10+ seconds
    # down to ~1.012 seconds
    A = sorted(map(int, raw_input().split()), reverse = True)
    sA = sum(A)
    if sA == 0:
        return "YES"
    elif X==0:
        return "NO"
    elif sA > X*2:
        return "NO"
    anslist = []
    tX = X
    while not anslist:
        findSum(anslist, tX, A)
        tX-=1
    if sA-sum(anslist[0]) > X:
        return "NO"
    return "YES"

if __name__ == "__main__":
    for testcase in xrange(int(raw_input())):
        print amazing_test()
