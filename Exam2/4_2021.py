# 1 ,2 , 4, 7 , 11

def func(n):
    if n == 1:
        return 1
    else:
        return func(n-1) + (n-1)

while True:
    x = int(input('enter a number:'))
    if x == -1:
        print('Finished')
        break
    if x < 1:
        print('enter a number greater than or equal 1')
    else:
        output = func(x)
        print(output)
