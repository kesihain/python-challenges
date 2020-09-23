def factorial_loop(n):
    val = 1
    for num in range(1,n+1):
        val = val*num
    return val

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n*factorial_recursive(n-1)

def fib_loop(index):
    arr = [0,1]
    for i in range(0,index-1):
        arr.append(arr[i]+arr[i+1])
    return arr[index]

def fib_recursive(n,val1=0,val2=1):
    if n==0:
        return val1
    if n==1:
        return val2
    else:
        return fib_recursive(n-1,val2,val1+val2)
        
print(f"Factorial Loop: {factorial_loop(5)}")
print(f"Factorial Recursive: {factorial_recursive(5)}")
print(f"Fibonacci Loop: {fib_loop(1)}")
print(f"Fibonacci Recursive: {fib_recursive(8)}")