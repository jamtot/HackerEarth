def allvowels(N):
    vowels=['a','e','i','o','u']
    stringy=raw_input()
    for i in xrange(N):
        if stringy[i] in vowels:
             vowels.pop(vowels.index(stringy[i]))
        if len(vowels)<1:
            return "YES"
    else:
        return "NO"        

if __name__ == "__main__":
    N=int(raw_input())
    print allvowels(N)
