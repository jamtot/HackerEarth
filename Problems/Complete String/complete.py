import string 
if __name__ == "__main__":
    letters = list(string.ascii_lowercase)
    print raw_input().lower()
    for i in xrange(int(raw_input())):
        if sorted({l for l in raw_input().lower()}) == letters:
            print "YES"
        else:
            print "NO"
