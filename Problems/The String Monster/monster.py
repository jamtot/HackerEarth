from itertools import combinations

def stringy(stringtoget, strings):
    stringtoget=sorted(stringtoget)
    strlen = len(stringtoget) 
    strlens = len(strings)
    for i in xrange(strlens):
        for perm in combinations(strings, i):
            perm="".join(perm)
            if len(perm) == strlen:
                if stringtoget==sorted(perm):
                    return "YES"
    else:
            return "NO"
    

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        N = int(raw_input())
        strings = []
        for i in xrange(N):
            strings.append(raw_input())
        stringtoget = raw_input()
        print stringy(stringtoget, strings)
