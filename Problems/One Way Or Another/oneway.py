def checkparity(n):
    ruledict={}
    inputs=[]
    for coords in xrange(n):
        inputs.append(raw_input())
    for inp in inputs:
        r,c,x = map(int,inp.split())
        if ((r%2),(c%2)) in ruledict:
            if ruledict[((r%2),(c%2))] != (x%2):
                return "No"
        else:    
            ruledict[((r%2),(c%2))]=(x%2)
            ruledict[((not r%2),(not c%2))]=(x%2)
            ruledict[((r%2),(not c%2))]=(not x%2)
            ruledict[((not r%2),(c%2))]=(not x%2)
    else:
        return "Yes"

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print checkparity(int(raw_input()))
