# link to problem: https://www.hackerrank.com/challenges/3d-surface-area/problem


def check_cube_sides(i,j,n):
    conditions = {
        'top': n == A[i][j],
        'bottom': n == 1,
        'first column': (n > A[i][j - 1] if j-1 >= 0 else j == 0),
        'second column': (n > A[i][j + 1] if j+1 < W else j == W-1),
        'first row': (n > A[i - 1][j] if i-1 >= 0 else i == 0),
        'second row': (n > A[i + 1][j] if i+1 < H else i == H-1),
    }
    cube_area = list(conditions.values()).count(True)
    return cube_area


def surface_area(A):
    area = 0
    for i in range(H):
        for j in range(W):
            cubes_in_cell = A[i][j]
            for n in range(1, cubes_in_cell+1):
                cube_area = check_cube_sides(i,j,n)
                area += cube_area
    return area


first_multiple_input = input().rstrip().split()
H, W = int(first_multiple_input[0]), int(first_multiple_input[1])
A = []
for _ in range(H):
    A.append(list(map(int, input().rstrip().split())))

result = surface_area(A)
print(result)
