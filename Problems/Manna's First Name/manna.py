def namecount(string):
    suvocount=string.count('SUVO')
    suvojitcount=string.count('SUVOJIT')
    return 'SUVO = %d, SUVOJIT = %d' % (suvocount-suvojitcount,suvojitcount)

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print namecount(raw_input())
