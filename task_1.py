
# Fibonacci sequence with cache dict which store previous computation results  
def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci


fib = caching_fibonacci()

# Example usage
assert fib(10) == 55
assert fib(15) == 610 



# Fibonacci sequence using generator 
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci_generator()

# Example usage
assert next(fib) == 0
assert next(fib) == 1
assert next(fib) == 1
assert next(fib) == 2
