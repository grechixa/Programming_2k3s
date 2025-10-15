def factorial(n: int, res=1) -> dict:
    if n == 1:
        return {'1', res}
    return factorial(n-1, res*n)

print(factorial(5))