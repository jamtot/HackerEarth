if __name__ == "__main__":
    demand = raw_input()
    for i in xrange(int(raw_input())):
        index1,index2 = map(lambda x: x-1, map(int, raw_input().split()))
        dlen = len(demand)
        if demand[index1%dlen] == demand[index2%dlen]:
            print "Yes"
        else:
            print "No"
