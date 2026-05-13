def fibo(n):
    if n > 2:
        return fibo(n - 1) + fibo(n - 2)
    else:
        return 1
    
print(fibo(4))