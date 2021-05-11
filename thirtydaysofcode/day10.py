# link to problem: https://www.hackerrank.com/challenges/30-binary-numbers/problem

n = int(input().strip())
power = 0
binary_str = ''
while 2 ** power <= n:
    power += 1
power -= 1

while power >= 0:
    if n - 2 ** power >= 0:
        n = n - 2 ** power
        binary_str += '1'
    else:
        binary_str += '0'
    power -= 1

binary_list = filter(lambda x: x != '', binary_str.split('0'))
print(len(max(binary_list)))