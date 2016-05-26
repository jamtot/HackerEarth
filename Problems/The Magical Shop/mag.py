def potions(inp, days):
    potions,modulo = inp
    total=0
    for i in xrange(len(days)):
        if days[i] == '1':
            total=(total+potions)%modulo
        potions = (potions*potions)%modulo
    return total
    #return sum([potions**(i+1) if days[i]=='1' else 0 for i in xrange(len(days))])%modulo
    
if __name__ == "__main__":
    print potions(map(int,raw_input().split()), raw_input() )
    
