# link to problem: https://www.hackerrank.com/challenges/30-arrays/problem

n = int(input().strip())

arr = list(map(int, input().rstrip().split()))
for i in range(n-1, -1, -1):
    print(arr[i], end=' ')
