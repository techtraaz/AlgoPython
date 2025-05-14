
def max_heapify(A , i , heap_size):
   
    left = 2 * i
    right = 2 * i + 1

    if left <= heap_size and A[left] > A[i]:
        largest = left
    else:
        largest = i
    
    if right <= heap_size and A[right] > A[largest]:
        largest = right

    if largest != i:
        A[i] , A[largest] = A[largest] , A[i]
        max_heapify(A,largest,heap_size)

def build_max_heap(A):
    heap_size = len(A) - 1
    for i in range(heap_size //2 , 0 , -1):
        max_heapify(A,i,heap_size)




def heapsort(A):
    build_max_heap(A)
    heap_size = len(A)-1
    for i in range(heap_size , 1 ,-1):
        A[1] , A[i] = A[i] , A[1]
        heap_size -= 1
        max_heapify(A,1,heap_size)

A = [None,90,4,12,179,23,8]
heapsort(A)
print(A[1:])

