# 1. Initial estimate of how long it will take you to code and test, ready for submission
#   There are two obvious solutions:
#   Directed graphs - very efficient but no estimation for the time to code it
#   Hardcoded check of all combinations - not a smooth solution but possibly faster one to implement (2-4 hours).
#   Not too demanding for any computer since the combinations are only 3*24*24*24
# 2. Actual time you take:
#   2 hours.

positions = [
      [0, 1, 2, 3, 4, 5],
      [0, 1, 5, 4, 2, 3],
      [0, 1, 3, 2, 5, 4],
      [0, 1, 4, 5, 3, 2],
      [1, 0, 2, 3, 5, 4],
      [1, 0, 4, 5, 2, 3],
      [1, 0, 3, 2, 4, 5],
      [1, 0, 5, 4, 3, 2],
      [2, 3, 0, 1, 4, 5],
      [2, 3, 5, 4, 0, 1],
      [2, 3, 1, 0, 5, 4],
      [2, 3, 4, 5, 1, 0],
      [3, 2, 0, 1, 5, 4],
      [3, 2, 4, 5, 0, 1],
      [3, 2, 1, 0, 4, 5],
      [3, 2, 5, 4, 1, 0],
      [4, 5, 0, 1, 2, 3],
      [4, 5, 3, 2, 0, 1],
      [4, 5, 1, 0, 3, 2],
      [4, 5, 2, 3, 1, 0],
      [5, 4, 0, 1, 3, 2],
      [5, 4, 2, 3, 0, 1],
      [5, 4, 1, 0, 2, 3],
      [5, 4, 3, 2, 1, 0]
]
solutions = []
counter = 0
cubes_arr = []
cubes = input("Enter colors of opposing sides for 4 cubes: ").upper().split(',')


def cubes_positions(cube, jump):
    flips = []
    for i in range(0, 24, jump):
        current_rotation = []
        for y in range(6):
            current_rotation.append(cube[positions[i][y]])
        flips.append(current_rotation)
    return flips


def check_solution(*cube):
    for k in range(3):
        for m in range(k+1, 4):
            if cube[k][2] == cube[m][2]:
                return "False"
            if cube[k][3] == cube[m][3]:
                return "False"
            if cube[k][4] == cube[m][4]:
                return "False"
            if cube[k][5] == cube[m][5]:
                return "False"
    return "True"


for cube in cubes:
    cubes_arr.append(list(cube))

try:
    for cube1 in cubes_positions(cubes_arr[0], 8):
        for cube2 in cubes_positions(cubes_arr[1], 1):
            for cube3 in cubes_positions(cubes_arr[2], 1):
                for cube4 in cubes_positions(cubes_arr[3], 1):
                    if check_solution(cube1, cube2, cube3, cube4) == "True":
                        counter += 1
                        solutions.append([cube1, cube2, cube3, cube4])
except:
    print("Check input.")
    quit()

print(f'Possible solutions: {counter}\n')
print('top, bottom, front, back, left, right\n')
for solution in solutions:
    for x in range(4):
        print(''.join(solution[x]))
    print()
