def quicksort(arr,start,end):
    if(start<end):
        mid = partition(arr,start,end)
        quicksort(arr,start,mid-1)
        quicksort(arr,mid+1,end)



def partition(arr,start,end):
    x = arr[end]
    i = start -1
    for j in range(start,end):
        if arr[j] <= x:
            i += 1
            arr[i] , arr[j] = arr[j] , arr[i]
    arr[i+1] , arr[end] = arr[end] , arr[i+1]
    return i +1

if __name__ == "__main__":
    arr = [10,80,30,90,40,50,70]
    quicksort(arr,0,len(arr)-1)
    print(arr)