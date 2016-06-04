def getarea(XYZ):
    # prism is A,B,C
    # X=A+B Y=B+C Z=A+C
    X,Y,Z = XYZ
    #A=2(wl+hl+hw)
    A = ((X+Z)-Y)/2
    B = ((X+Y)-Z)/2
    C = ((Y+Z)-X)/2
    return 2*(A*B+C*B+C*A)
    
if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print("%.2f" % round(getarea(map(float,raw_input().split())),2))
