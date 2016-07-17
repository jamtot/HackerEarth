def substr(string, possub):
    for l in possub:
        if l in string:
            return "YES"
    else: return "NO"

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print substr(raw_input(),raw_input())
