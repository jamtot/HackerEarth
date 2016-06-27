def invite_list(n):
    return "\n".join(sorted({raw_input() for i in xrange(n)}))

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print invite_list(int(raw_input()))
