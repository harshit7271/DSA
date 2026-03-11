# calling a fuction inside the same function, recursion is process of defining something in terms of itself

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)


print(factorial(5))


# fibonacci numbers

def fib(self, n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    """
    else:
        return self.fib(n-1) + self.fib(n-2)"""
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b
