def max_heapify(A,i):
    l = 2 * i
    r = 2 * i +1
    heap_size = len(A) - 1
    
    if l <= heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    
    if  r <= heap_size and A[r] > A[i]:
        largest = r

    if largest != i:
        A[i] , A[largest] = A[largest], A[i]
        max_heapify(A,largest)

A = [None, 16, 4, 10, 14, 7, 9, 3, 2, 8, 1] 
 # 1-based indexing

Aa = [None, 7, 24,19,21,14,3,10,2,11]
max_heapify(Aa, 2)
print(Aa)
