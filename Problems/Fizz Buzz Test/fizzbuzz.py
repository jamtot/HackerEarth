def fizzbuzz(n):
    output = ''
    if n%3==0:
        output+='Fizz'
    if n%5==0:
        output+='Buzz'
    if output == '':
        output=n
    return output

#or
def fb(n):
    if n%15==0:
        return "FizzBuzz"
    elif n%3==0:
        return "Fizz"
    elif n%5==0:
        return "Buzz"
    return n

if __name__ == "__main__":
    for i in xrange(1,101):
        print fb(i)
