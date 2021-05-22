# link to problem: https://www.hackerrank.com/challenges/queens-attack-2/problem

def count_boxes(dx, dy, q_coord, ob):
    current_count = 0
    queen_row, queen_col = q_coord[0], q_coord[1]
    queen_col += dx
    queen_row += dy
    while 1 <= queen_col <= n and 1 <= queen_row <= n:

        if [queen_row, queen_col] in ob:
            return current_count
        else:
            current_count += 1
        queen_col += dx
        queen_row += dy
    return current_count

def queensAttack(n, k, r_q, c_q, obstacles):
    moves = {
        'horizontal_left': count_boxes(dx=-1, dy=0, q_coord=(r_q, c_q), ob=obstacles),
        'horizontal_right': count_boxes(dx=+1, dy=0, q_coord=(r_q, c_q), ob=obstacles),
        'vertical_up': count_boxes(dx=0, dy=+1, q_coord=(r_q, c_q), ob=obstacles),
        'vertical_down': count_boxes(dx=0, dy=-1, q_coord=(r_q, c_q), ob=obstacles),
        'diag_down_right': count_boxes(dx=+1, dy=-1, q_coord=(r_q, c_q), ob=obstacles),
        'diag_down_left': count_boxes(dx=-1, dy=-1, q_coord=(r_q, c_q), ob=obstacles),
        'diag_up_right': count_boxes(dx=+1, dy=+1, q_coord=(r_q, c_q), ob=obstacles),
        'diag_up_left': count_boxes(dx=-1, dy=+1, q_coord=(r_q, c_q), ob=obstacles),
    }
    count = sum(moves.values())
    return count


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])

second_multiple_input = input().rstrip().split()
r_q = int(second_multiple_input[0])
c_q = int(second_multiple_input[1])

obstacles = []
for _ in range(k):
    obstacles.append(list(map(int, input().rstrip().split())))

result = queensAttack(n, k, r_q, c_q, obstacles)
print(result)