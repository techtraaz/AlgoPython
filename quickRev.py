
def quicksort(arr,start,end):
    if start<end:
        q = partition(arr,start,end)
        quicksort(arr,start,q-1)
        quicksort(arr,q+1,end)
    
def partition(arr,start,end):
    x = len(arr[end])
    i = start - 1
    for j in range(start,end):
        if len(arr[j]) >= x:
            i = i + 1
            arr[i] , arr[j] = arr[j] , arr[i]
    arr[i+1] , arr[end] = arr[end] , arr[i+1]
    return i+1

if __name__ == "__main__":
    array = ["john", "doe", "smith","desktop","srilanka"]
    quicksort(array,0,len(array)-1)
    print(array)