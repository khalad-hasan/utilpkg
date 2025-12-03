import math

def factorial(n):
    if n < 0:
        raise ValueError("Negative numbers not allowed")
    return math.factorial(n)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    if n < 0:
        raise ValueError("Negative numbers not allowed")
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def gcd(a, b):
    return math.gcd(a, b)
