"""
Author: Jonathan Morris
Holiday Season
ttps://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/holiday-season-ab957deb/
"""

n = int(input())
line = str(input())
count = 0
for a in range(n):
    for b in range(a+1,n):
        for c in range(b+1,n):
            for d in range(c+1,n):
                if line[a]==line[c] and line[b] == line[d]:
                    count+=1
print(count)
