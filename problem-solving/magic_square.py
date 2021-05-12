# link to problem: https://www.hackerrank.com/challenges/magic-square-forming/problem

from collections import Counter
from itertools import combinations, permutations

def formingMagicSquare(s):
    cost = []

    possible_numbers = [n for n in range(1, 10)]
    possible_combinations = [comb for comb in combinations(possible_numbers, 3) if sum(comb) == 15]
    possible_matrices = []

    for m in combinations(possible_combinations, 3):
        full_list = [j for row in m for j in row]
        if [str(v) for v in Counter(full_list).values()].count('1') == 9:
            possible_matrices.append(list(m))

    valid_matrices = []
    for matrix in possible_matrices:
        for c in permutations(set(matrix), 3):
            for p in permutations(c[0], 3):
                for k in permutations(c[1], 3):
                    for l in permutations(c[2], 3):
                        curr_c = [p, k, l]
                        conditions = {
                            'first_true': p[0] + k[0] + l[0] == 15,
                            'second_true': p[1] + k[1] + l[1] == 15,
                            'third_true': p[2] + k[2] + l[2] == 15,
                            'first_diag_true': p[0] + k[1] + l[2] == 15,
                            'second_diag_true': p[2] + k[1] + l[0] == 15
                        }
                        if conditions["first_true"] and conditions["second_true"] and conditions["third_true"] and conditions["first_diag_true"] and conditions["second_diag_true"]:
                            valid_matrices.append(curr_c)

    for m in valid_matrices:
        current_sum = 0
        for r in range(3):
            for c in range(3):
                current_sum += abs(s[r][c] - m[r][c])
        cost.append(current_sum)
    return min(cost)


s = []
for _ in range(3):
    s.append(list(map(int, input().rstrip().split())))

result = formingMagicSquare(s)
print(result)