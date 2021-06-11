# link to problem: https://www.hackerrank.com/challenges/the-time-in-words/problem

nums = ["o\' clock", "one minute", "two minutes", "three minutes", "four minutes",
        "five minutes", "six minutes", "seven minutes", "eight minutes", "nine minutes",
        "ten minutes", "eleven minutes", "twelve minutes", "thirteen minutes",
        "fourteen minutes", "quarter", "sixteen minutes",
        "seventeen minutes", "eighteen", "nineteen minutes",
        "twenty minutes", "twenty one minutes", "twenty two minutes",
        "twenty three minutes", "twenty four minutes",
        "twenty five minutes", "twenty six minutes", "twenty seven minutes",
        "twenty eight minutes", "twenty nine minutes", "half"]

def minutesInWords(m, word):
    minutes = f'{nums[m]} {word}'
    return minutes

def timeInWords(h, m):
    hour = nums[h].split(' ')[0] if m <= 30 else nums[h+1].split(' ')[0]
    if m == 0:
        minutes = nums[m]
    elif 1 <= m <= 30:
        minutes = minutesInWords(m, 'past')
    else:
        minutes = minutesInWords(60-m, 'to')

    text = [hour, minutes] if m == 0 else [minutes, hour]
    return ' '.join(text)


h = int(input().strip())
m = int(input().strip())

print(timeInWords(h, m))