# link to problem: https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem

if __name__ == '__main__':
    try:
        print(int(input().strip()))
    except ValueError:
        print('Bad String')