# link to problem: https://www.hackerrank.com/challenges/30-recursion/problem

def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1)


num = int(input().strip())
print(factorial(num))