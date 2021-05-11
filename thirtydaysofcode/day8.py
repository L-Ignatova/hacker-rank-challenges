# link to problem: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

dict = dict()

n = int(input())
for _ in range(n):
    entry = input().split(' ')
    name, num = entry[0], entry[1]
    dict[name] = num

for _ in range(n):
    try:
        inp = input()
        if inp in dict.keys():
            print(f'{inp}={dict[inp]}')
        else:
            print('Not found')
    except EOFError as e:
        break
