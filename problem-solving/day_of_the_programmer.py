# link to problem: https://www.hackerrank.com/challenges/day-of-the-programmer/problem

days_of_the_year = {'01': 31, '02': 28, '03': 31,
                    '04': 30, '05': 31, '06': 30,
                    '07': 31, '08': 31, '09': 30,
                    '10': 31, '11': 30, '12': 31
                    }
day_to_find = 256


def get_day_month(year, leap):
    current_day = day_to_find
    if leap:
        days_of_the_year['02'] = 29

    for key, val in days_of_the_year.items():
        if current_day - val > 0:
            current_day -= val
            continue
        month = key
        day = current_day
        break

    return f'{day}.{month}.{year}'


def dayOfProgrammer(year):
    leap = False
    if 1700 <= year <= 1917:
        if year % 4 == 0:
            leap = True
    elif year == 1918:
        days_of_the_year['02'] = days_of_the_year['02'] - 13
        return get_day_month(year, leap)
    elif year > 1918:
        if year % 4 == 0 and year % 100 != 0:
            leap = True
        elif year % 100 == 0 and year % 400 == 0:
            leap = True
    return get_day_month(year, leap)


year = int(input().strip())
result = dayOfProgrammer(year)
print(result)

# or just return one of the 3 possible cases depending on the conditions met
