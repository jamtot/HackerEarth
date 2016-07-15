def fortune(binary):
    count=0
    cur=''
    for n in binary:
        if cur==n:
            count+=1
        else:
            cur=n
            count=1
        if count==6:
            return "Sorry, sorry!"
    else:
        return "Good luck!"

if __name__ == "__main__":
    print fortune(raw_input())
