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
    assert myprime(5, "10 5 3 15 16") == "5 3 16"
    print myprime(int(raw_input()), raw_input())
