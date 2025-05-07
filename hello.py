def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            # Swap elements
            array[i], array[j] = array[j], array[i]
    
    # Place the pivot in its correct position
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quicksort(array, low, high):
    if low < high:
        # Find the pivot index
        pi = partition(array, low, high)
        
        # Recursively sort elements before and after partition
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)

data = [1, 7, 4, 1, 10, 9, -2]

print('Unsorted array:', data)

size = len(data)
quicksort(data, 0, size - 1)

print('Sorted array:', data)
