// Fórmula Matemática
from math import sqrt


def F(n):
    return ((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5))


def Fibonacci(startNumber, endNumber):
    n = 0
    cur = F(n)
    while cur <= endNumber:
        if startNumber <= cur:
            print(cur)
        n += 1
        cur = F(n)


Fibonacci(1, 100)

//Iterativ Loop For 
def fibonacciIterativ(n):
    a = 1
    b = 1
    if n == 1:
        print("0")
    elif n == 2:
        print("0", "1")
    else:
        print("0")
        print(a)
        print(b)
        for i in range(n - 3):
            total = a + b
            b = a
            a = total
            print(total)


fibonacciIterativ(8)

//recursiv

def fibonacciRecursiv(n):
    if n > 1:
        return fibonacciRecursiv(n - 1) + fibonacciRecursiv(n - 2)
    return n


for i in range(10):
    print(fibonacciRecursiv(i))

//Dinamic

def fibonacci(num):
    arr = [0, 1]
    if num == 1:
        print("0")
    elif num == 2:
        print("[0,", "1]")
    else:
        while len(arr) < num:
            arr.append(0)
        if num == 0 or num == 1:
            return 1
        else:
            arr[0] = 0
            arr[1] = 1
            for i in range(2, num):
                arr[i] = arr[i - 1] + arr[i - 2]
            print(arr)


fibonacci(10)
