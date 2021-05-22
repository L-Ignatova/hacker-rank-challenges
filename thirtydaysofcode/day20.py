# link to problem: https://www.hackerrank.com/challenges/30-sorting/problem

n = int(input().strip())

a = list(map(int, input().rstrip().split()))
swaps = 0
sorted_list = False

while not sorted_list:
    curr_swaps = swaps
    for i in range(len(a) - 1):
        if a[i] >= a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            swaps += 1
    if curr_swaps == swaps:
        sorted_list = True

print(f'Array is sorted in {swaps} swaps.\nFirst Element: {a[0]}\nLast Element: {a[len(a) - 1]}')
