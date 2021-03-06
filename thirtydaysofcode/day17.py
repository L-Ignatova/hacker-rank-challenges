#link to problem: https://www.hackerrank.com/challenges/30-more-exceptions/problem

class Calculator:
    @staticmethod
    def power(num, pow):
        if n < 0 or p < 0:
            raise Exception('n and p should be non-negative')
        return num ** pow


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)