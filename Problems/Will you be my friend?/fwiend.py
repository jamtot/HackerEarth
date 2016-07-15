from fractions import gcd

def friends(integer, kids, kidnums):
    return sum([1 if gcd(integer,n)>1 else 0 for n in kidnums]) 

if __name__ == "__main__":
    print friends(int(raw_input()),int(raw_input()),map(int,raw_input().split())) 
