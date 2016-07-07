def strange_add(Ns):
    return reverse(reverse(Ns[0])+reverse(Ns[1]))

def reverse(N):
    return int(str(N)[::-1])

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print strange_add(map(int,raw_input().split()))
