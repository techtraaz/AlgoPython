def quicksort_v1(array, start, end):
    if start < end:
        q = partition(array, start, end)
        quicksort_v1(array, start, q - 1)
        quicksort_v1(array, q + 1, end)

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[low] <= pivot:
            low += 1
        while low <= high and array[high] >= pivot:
            high -= 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]
    return high

if __name__ == "__main__":
    arry = [10, 450, 24, 78, 2, 14]
    quicksort_v1(arry, 0, len(arry) - 1)
    print(arry)
