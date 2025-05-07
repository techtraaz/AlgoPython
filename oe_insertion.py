
def insertion_odd_even(Array):
    for j in range(1,len(Array)):
        key = Array[j]

        i = j - 1
        while i>= 0 and  (Array[i] % 2 > key % 2 or (Array[i] % 2 == key % 2 and Array[i] > key)) :
             
             Array[i+1] = Array[i]
             i = i - 1 
             Array[i+1] = key
            

    return Array


if __name__ == "__main__":
    a = [9,2,1,8,4,7]
    insertion_odd_even(a)
    print(a)