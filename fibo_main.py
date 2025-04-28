import fibo_module

num_terms = int(input("Enter the number of terms for Fibonacci series: "))

fib_series = fibo_module.fibonacci(num_terms)

print(f"The Fibonacci series up to {num_terms} terms is:")
print(fib_series)
