

def mul(M,n):
    if n == 1:
        return M
    else:
        return M + mul(M,(n-1))


while True:
    M = int(input('Enter M:'))
    n = int(input('Enter n:'))

    res = mul(M,n)

    print(f'multiply of {M} x {n} is {res}')
