def fac(n):
    if n==1:
        return 1
    else:
        return fac(n-1) * n

if __name__ == "__main__":
    print fac(int(raw_input()))
