# link to problem: https://www.hackerrank.com/challenges/sock-merchant/problem
from collections import Counter


def sockMerchant(n, ar):
    socks_by_color = Counter(ar)
    pairs_dict = {}
    for key, val in socks_by_color.items():
        if val // 2 >= 1:
            pairs_dict[key] = val // 2
    return sum(pairs_dict.values())


n = int(input().strip())
ar = list(map(int, input().rstrip().split()))
result = sockMerchant(n, ar)
print(result)