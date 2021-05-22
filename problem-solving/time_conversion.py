# link to problem: https://www.hackerrank.com/challenges/time-conversion/problem

def timeConversion(s):
    time = s.split(':')
    hours, minutes, seconds = time[0], time[1], time[2]
    seconds = seconds[:len(seconds)-2]
    time_of_day = s[len(s)-2:]
    if time_of_day == 'AM':
        if hours == '12':
            hours = '00'
    else:
        if hours != '12':
            hours = str(int(hours) + 12)
    return f'{hours}:{minutes}:{seconds}'


s = input()
result = timeConversion(s)
print(result)