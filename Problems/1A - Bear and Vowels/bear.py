vowels=['a','e','i','o','u','y']

def pronounce(word):
    vcount,ccount,count=0,0,0
    for l in word:
        if l in vowels:
            vcount+=1
            count=0
        else:
            count+=1
            ccount+=1
        if count>2:
            return 'hard'
    else:
        if ccount>vcount:
            return 'hard'
        else: return 'easy'

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print pronounce(raw_input())
