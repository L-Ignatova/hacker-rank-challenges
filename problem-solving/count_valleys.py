# link to problem: https://www.hackerrank.com/challenges/counting-valleys


def countingValleys(path):
    units = {'U': 1, 'D': -1}
    sea_level, valleys = 0, 0
    for step in path:
        sea_level += units[step]
        if step == 'U' and sea_level == 0:
            valleys += 1
    return valleys


steps = int(input().strip())
path = input()
print(countingValleys(path))
