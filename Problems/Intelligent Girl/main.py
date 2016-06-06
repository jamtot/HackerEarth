if __name__ == "__main__":
    count = 0
    nstring = ''
    for i in raw_input()[::-1]:
        if int(i)%2==0:
            count+=1
        nstring=str(count)+' '+nstring 
    print nstring
