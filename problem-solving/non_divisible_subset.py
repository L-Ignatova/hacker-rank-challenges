# link to problem: https://www.hackerrank.com/challenges/non-divisible-subset/problem

from collections import Counter


def nonDivisibleSubset(k, s):
    if k == 0 or k == 1:
        return 1
    s_remainders = [r % k for r in s]
    dict = Counter(s_remainders)
    res = []
    for i in range(0, len(s)):
        cur_num = s_remainders[i]
        other = k - cur_num
        if dict[cur_num] < dict[other]:
            continue
        if cur_num == other or cur_num == 0:
            if cur_num not in res:
                res.append(cur_num)
        else:
            res.append(cur_num)
    return len(res)


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])

s = list(map(int, input().rstrip().split()))
result = nonDivisibleSubset(k, s)
print(result)
