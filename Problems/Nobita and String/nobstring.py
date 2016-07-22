def reversal(stringy):
    return ' '.join(stringy.split()[::-1])

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print reversal(raw_input())
