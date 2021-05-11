# link to problem: https://www.hackerrank.com/challenges/30-review-loop/problem

n = int(input())

for _ in range(n):
    string = input()
    even = ''
    odd = ''
    for i, letter in enumerate(string):
        if (i+1) % 2 != 0:
            odd += letter
        else:
            even += letter
    print(f'{odd} {even}')
