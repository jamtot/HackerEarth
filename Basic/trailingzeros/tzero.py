def fac(n):
    if n<1:
        return n
    else: 
        ans = 1
        for i in xrange(n,1,-1):
            ans*=i
        return ans

def checkzeros(num):
    bnum = str(num)[::-1]
    zeros=0
    for n in bnum:
        if n == "0":
            zeros+=1
        else: break
    return zeros

def faczeros(n):
    return checkzeros(fac(n))
      
if __name__ == "__main__":
    print faczeros(int(raw_input()))
