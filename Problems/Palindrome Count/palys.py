def palicount(string):
    slen = len(string)
    count=0
    for i in xrange(slen):
        for j in xrange(i+1,slen+1):
            if pal(string[i:j]):
                print string[i:j]
                count+=1
    return count
    
def pal(string):
    for i in xrange(len(string)):
        if string[i]!=string[-(i+1)]:
            return False
    else:
        return True
    

if __name__ == "__main__":
    print palicount(raw_input())
