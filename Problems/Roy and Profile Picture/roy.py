def upload(L, W, H):
    if L > W or L > H:
        print "UPLOAD ANOTHER"
    elif W==H:
        print "ACCEPTED"
    else:
        print "CROP IT"

if __name__ == "__main__":
    L = int(raw_input())
    N = int(raw_input())
    for n in xrange(N):
        W_H = map(int,raw_input().split())
        upload(L, W_H[0], W_H[1])
