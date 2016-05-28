def quickSort(alen, array):
    quickSortHelper(array,0,alen-1)
    return array

def quickSortHelper(array,first,last):
    if first<last:
        splitpoint = partition(array,first,last)
        quickSortHelper(array,first,splitpoint-1)
        quickSortHelper(array,splitpoint+1,last)

def partition(array,first,last):
    pivotvalue = array[first]
    leftmark = first+1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and array[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while array[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
        if rightmark < leftmark:
            done = True
        else:
            array[leftmark],array[rightmark]=array[rightmark],array[leftmark]
    array[first],array[rightmark] = array[rightmark],array[first]
    return rightmark

def query(A, n):
    Alen = len(A)
    if Alen > 1:
        if n < A[Alen/2]:
            query(A[:Alen/2],n)
        elif n > A[Alen/2]:
            query(A[Alen/2:],n)
        elif n == A[Alen/2]:
            print "YES"
            return
    else:
        if n == A[0]:
            print "YES"
        else:
            print "NO"
        return
        
def query2(A, N, num):
    Alen = len(A)
    i=Alen/2
    while True:
        if Alen == 1:
            if A[0]==num: return "YES"
            else: return "NO"
        if num < A[Alen/2]:
            A = A[:Alen/2]
            Alen = Alen/2
        elif num > A[Alen/2]:
            A = A[Alen/2:]
            Alen = Alen-(Alen/2)
        elif num == A[Alen/2]:
            return "YES"

#previous attempts above weren't passing large array testcases
        
from bisect import bisect_left

def binary_search(a,x,alen,lo=0,hi=None):
    hi = hi if hi is not None else N
    pos = bisect_left(a,x,lo,hi)
    return ("YES" if pos != hi and a[pos] == x else "NO")      

if __name__ == "__main__":
    N,Q = map(int,raw_input().split())
    A = sorted(raw_input().split())
    for i in xrange(Q):
        num = raw_input()
        print binary_search(A,num,N)
