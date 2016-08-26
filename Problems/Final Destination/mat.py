def final(dirs):
    x,y=0,0
    for l in dirs:
        if l=='L':
            x-=1
        elif l=='R':
            x+=1
        elif l=='U':
            y+=1
        elif l=='D':
            y-=1
    print x,y

if __name__ == "__main__":
    final(raw_input())
