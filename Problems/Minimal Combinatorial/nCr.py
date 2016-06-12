def f(n):
  if n==0:return 1
  else:return n*f(n-1)
def c(x):
  return f(x[0])/(f(x[1])*f(x[0]-x[1]))
for tc in xrange(int(raw_input())):print c(map(int,raw_input().split()))
