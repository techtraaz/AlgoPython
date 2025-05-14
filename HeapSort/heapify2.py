# Global heap_size variable
heap_size = 0

def heapify(A, i):
    global heap_size
    left = 2 * i
    right = 2 * i + 1

    # Find the largest among root, left child, and right child
    if left <= heap_size and A[left] > A[i]:
        largest = left
    else:
        largest = i

    if right <= heap_size and A[right] > A[largest]:
        largest = right

    # If the largest is not root, swap and recursively heapify the affected subtree
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, largest)

def build_max_heap(A):
    global heap_size
    heap_size = len(A) - 1
    for i in range(heap_size // 2, 0, -1):
        heapify(A, i)

def heapsort(A):
    global heap_size
    heap_size = len(A) - 1
    build_max_heap(A)
    for i in range(heap_size, 1, -1):
        A[1], A[i] = A[i], A[1]  # Swap max with the last item
        heap_size -= 1
        heapify(A, 1)

# Example usage
A = [None, 47, 4, 19, 21, 14, 3, 30, 2, 13, 11]

print("Original:", A[1:])
heapsort(A)
print("Sorted:", A[1:])
