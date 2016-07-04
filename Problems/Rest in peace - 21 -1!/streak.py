def broken(n):
    if (n!=0 and n%21==0) or "21" in str(n):
        return "The streak is broken!"
    else:
        return "The streak lives still in our heart!"

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print broken(int(raw_input()))
        
