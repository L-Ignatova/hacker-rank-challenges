# link to problem: https://www.hackerrank.com/challenges/30-2d-arrays/problem
import sys

arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

sums = -sys.maxsize
for i in range(4):
    for j in range(4):
        top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        middle = arr[i+1][j+1]
        bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        if top+middle+bottom > sums:
            sums = top + middle + bottom

print(sums)