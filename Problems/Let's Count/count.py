def r_gcd(a,b):
    if b==0: 
        return a
    else:
        return gcd(b,a%b)

def i_gcd(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def threegcd(a,b,c):
    return gcd(gcd(a,b),c)

if __name__ == "__main__":
    facdict={}
    for tc in xrange(int(raw_input())):
        a,b,c = map(int,raw_input().split())
        jeeseedee=threegcd(a,b,c)
        i=1
        factors=1
        if jeeseedee not in facdict:
            while i<=jeeseedee/2:
                if jeeseedee%i==0:
                    factors+=1
                    facdict[jeeseedee]=factors
                i+=1
            print factors
            facdict[jeeseedee]=factors
        else:
            print facdict[jeeseedee]
