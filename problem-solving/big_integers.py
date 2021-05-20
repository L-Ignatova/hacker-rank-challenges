# link to problem: https://www.hackerrank.com/challenges/extra-long-factorials/problem

def extraLongFactorials(n):
    if n == 1:
        return 1
    return n * extraLongFactorials(n-1)

if __name__ == '__main__':
    n = int(input().strip())
    print(extraLongFactorials(n))
