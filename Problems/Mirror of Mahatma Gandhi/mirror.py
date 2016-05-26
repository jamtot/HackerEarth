import re

def mirrored(n):
    if not re.search("[^108]",n) and n==n[::-1]:
        return "YES"
    return "NO" 
    
if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print mirrored(raw_input())
