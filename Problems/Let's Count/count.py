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
    for tc in xrange(int(raw_input())):
        a,b,c = map(int,raw_input().split())
        jeeseedee=threegcd(a,b,c)
        i=0
        factors=0
        while i<=jeeseedee/2:
            i+=1
            if jeeseedee%i==0:
                factors+=1
            
        print factors
