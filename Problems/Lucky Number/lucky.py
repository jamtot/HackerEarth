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

def find_y(luckynums):
    x = int(raw_input())

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print find_y(map(int,raw_input().split()))
