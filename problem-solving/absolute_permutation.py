# link to problem: https://www.hackerrank.com/challenges/absolute-permutation/problem


def absolutePermutation(n, k):
    numbers = [_ for _ in range(1, n+1)]
    permutation = []
    if k == 0:
        return numbers
    if (n / k) % 2 != 0:
        return [-1]

    index = 0
    addition = True
    while len(permutation) < len(numbers):
        if addition:
            for i in range(k):
                permutation.append(numbers[index + i] + k)
                addition = False
        else:
            for i in range(k):
                permutation.append(numbers[index + i] - k)
                addition = True
        index += k
    return permutation


t = int(input().strip())
for t_itr in range(t):
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    result = absolutePermutation(n, k)
    print(result)