def fac(n):
    if n == 0: return 1
    else:
        return n * fac(n-1)

def smallfacs(T):
    for t in xrange(T):
        print fac(int(raw_input()))

if __name__ == "__main__":
    smallfacs(int(raw_input()))
