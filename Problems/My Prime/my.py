def myprime(N,S):
    S = [int(i) for i in S.split(" ")[:N]]
    myprimes = []
    for i in S:
        divs = 0
        for j in S:
            if i is not j and i >= j:
                if i%j==0:
                    divs+=1
                    break
        if divs==0: myprimes.append(i)
    return " ".join(map(str,myprimes))
                 

if __name__ == "__main__":
    print myprime(int(raw_input()), raw_input())
