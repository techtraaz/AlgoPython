def countdown(n):
    if n == 0 :
        print("done")
    else:
        print(n)
        countdown(n-1)

countdown(3)

def rangetest(x):
    i = 0 
    for i in range(i,x):
        print(i)

if __name__ == "__main__":
    rangetest(5)