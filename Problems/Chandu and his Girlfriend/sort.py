def insertionsort(alen, array):
    for i in xrange(1, alen):
        j=i
        while j > 0 and array[j-1] < array[j]:
            array[j],array[j-1] = array[j-1],array[j]
            j-=1
    return ' '.join(map(str,array))

def quickSort(alen, array):
    quickSortHelper(array,0,alen-1)
    return ' '.join(map(str,array))

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
        while leftmark <= rightmark and array[leftmark] >= pivotvalue:
            leftmark = leftmark + 1
        while array[rightmark] <= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
        if rightmark < leftmark:
            done = True
        else:
            array[leftmark],array[rightmark]=array[rightmark],array[leftmark]
    array[first],array[rightmark] = array[rightmark],array[first]
    return rightmark

def psort(alen, array):
    return ' '.join(map(str,sorted(array,reverse=True)))
        
if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print quickSort(int(raw_input()), map(int,raw_input().split()))
