def chocbreak(N):
    bar = []
    for row in xrange(N):
        bar.extend(list(raw_input())[:N])
    rows,cols = [],[]
    for i in xrange(N):
        rows.append(sum([1 if bar[j] == '#' else 0 for j in xrange(N*i,N+(N*i))]))
        cols.append(sum([1 if bar[(N*j)+i] == '#' else 0 for j in xrange(N)]))
    for i in xrange(1,N):
        if (sum(rows[:i]) == sum(rows[i:])) or (sum(cols[:i]) == sum(cols[i:])):
            return 'YES'
    return 'NO'

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print chocbreak(int(raw_input()))


""" # too slow to complete the larger inputs quickly
from collections import Counter

def chocbreak(N):
    rows = []
    for row in xrange(N):
        rows.extend(list(raw_input())[:N])
    "" "cols = []
    for i in xrange(N):
        for j in xrange(N):
            cols.append(rows[(N*j)+i])"" "
    cols = [rows[(N*j)+i] for i in xrange(N) for j in xrange(N)]
    for i in xrange(N,N*N,N):
        c1 = Counter(rows[:i])
        c2 = Counter(rows[i:])
        c3 = Counter(cols[:i])
        c4 = Counter(cols[i:])
        if (c1['#'] == c2['#']) or (c3['#'] == c4['#']):
            return 'YES'
    return 'NO'
"""
