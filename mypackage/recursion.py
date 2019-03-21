def sum_array(array):
    if len(array)== 1:
        return array[0]
    else:
        return array[0]+sum_array(array[1:])

def Fibonacci(n):
    if n<0: 
        print("Wrong input") 
    # First Fibonacci number is 0 
    elif n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def reverse(word):
    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]
