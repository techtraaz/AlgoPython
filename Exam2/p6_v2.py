
def s(n):
    if n == 1:
        return 1
    return s(n-1)+n*n*n

res = s(3)
nn = 3
print(f'sum of first {nn} integers :' , res)
