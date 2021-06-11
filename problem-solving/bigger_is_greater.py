# link to problem: https://www.hackerrank.com/challenges/bigger-is-greater/problem

def biggerIsGreater(w):
    list_w = [l for l in w]
    if len(list_w) == 1:
        return 'no answer'
    for i in range(len(list_w)-1, 0, -1):
        current_letter = w[i]
        for j in range(i - 1, -1, -1):
            if w[j] < current_letter:
                list_w[j], list_w[i] = list_w[i], list_w[j]
                first = list_w[:j+1]
                second = sorted(list_w[j+1:])
                res_word = first + second
                return ''.join(res_word)
    return 'no answer'


T = int(input().strip())

for T_itr in range(T):
    w = input()
    result = biggerIsGreater(w)
    print(result)