# Fibonacci Sequence in three different approaches with input function:

# Fibonacci Sequence in three different approaches with input function:

# Approach 1: Using Recursion
def fibonacci_recursion(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

# Approach 2: Using Iteration
def fibonacci_iteration(n):
    if n == 1 or n == 2:
        return 1
    fib_sequence = [1, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[-1]

# Approach 3: Using Dynamic Programming
def fibonacci_dynamic(n):
    if n == 1 or n == 2:
        return 1
    fib_sequence = [1, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence[-1]

def get_fibonacci_number(n, approach):
    if n <= 0:
        return "Error: Nth position must be a positive integer."
    
    approaches = {
        "recursion": fibonacci_recursion,
        "iteration": fibonacci_iteration,
        "dynamic": fibonacci_dynamic
    }
    
    if approach in approaches:
        return approaches[approach](n)
    else:
        return "Error: Invalid approach selected."

n = int(input("Enter number in Nth position (positive integer): "))

if n <= 0:
    print("Error: Nth position must be a positive integer.")
else:
    # Approach 1
    result = get_fibonacci_number(n, "recursion")
    print(f"Approach 1 result: {result}")
    
    # Approach 2
    result = get_fibonacci_number(n, "iteration")
    print(f"Approach 2 result: {result}")
    
    # Approach 3
    result = get_fibonacci_number(n, "dynamic")
    print(f"Approach 3 result: {result}")