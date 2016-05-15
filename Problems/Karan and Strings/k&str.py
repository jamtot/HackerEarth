if __name__ == "__main__":
    for testcase in xrange(int(raw_input())):
        inp = raw_input()
        out=''
        current = ''
        for i in xrange(len(inp)):
            if current != inp[i]:
                current = inp[i]
                out+=current
        print out
