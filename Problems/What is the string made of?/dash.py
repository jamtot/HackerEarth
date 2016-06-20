dashdict = {'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6}

if __name__=="__main__":
    print sum([dashdict[i] for i in raw_input()])
