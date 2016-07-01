def caninvite(costs,money,peeps):
    for i in xrange(peeps):
        for j in xrange(i+1,peeps+1):
            sm = sum(costs[i:j])
            if sm==money:
                return "YES"
            elif sm>money:
                break
    else: return "NO"

def linearinvite(costs,money,peeps):
    pass

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        N,X = map(int,raw_input().split())
        costs = [int(raw_input()) for i in xrange(N)]
        print caninvite(costs,X,N)
        
        
