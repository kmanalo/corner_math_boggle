import numpy as np


def do_math_left_to_right(expression):
    digits = "0123456789"
    pieces = []

    i = 0
    for c in expression:
        if c in digits:
            try:
                pieces[i] += c
            except IndexError:
                pieces.append(c)
        elif c in {"+", "-", "*", "/"}:
            i += 1
            pieces.append(c)

    last_piece = pieces.pop(0)
    result = 0
    intermediates = ""
    for piece in pieces:
        result = eval(f"{last_piece}{piece}")
        intermediates += " " + str(result)
        last_piece = str(result)
    return intermediates, result


print(do_math_left_to_right(["1", "+", "2", "*", "3"]))

problem = [
    ["2", "+", "9", "/", "3"],
    ["+", "1", "*", "2", "*"],
    ["4", "*", "6", "*", "8"],
    ["-", "4", "/", "5", "-"],
    ["5", "+", "2", "*", "7"],
]

problem = [
    ["5", "/", "8", "+", "4"],
    ["-", "7", "*", "5", "+"],
    ["9", "/", "6", "*", "2"],
    ["*", "2", "/", "2", "-"],
    ["3", "*", "6", "+", "1"],
]

problem = np.array(problem)

files = [
    "8512_LL_UR.txt",
    "8512_LR_UL.txt",
    "8512_UL_LR.txt",
    "8512_UR_LL.txt",
    "8590_LL_LR.txt",
    "8590_LL_UL.txt",
    "8590_LR_LL.txt",
    "8590_LR_UR.txt",
    "8590_UL_LL.txt",
    "8590_UL_UR.txt",
    "8590_UR_LR.txt",
    "8590_UR_UL.txt",
]

for myfile in files:
    with open(myfile, "r") as f:
        for line in f:
            expression = []
            result = line.split()[2:][0].split(",")
            result = [int(i) - 1 for i in result]
            print()
            n = 2
            coords = list(tuple(result[i : i + n]) for i in range(0, len(result), n))
            for coord in coords:
                expression.append(str(problem[coord]))
            # print(coords)
            print(expression, do_math_left_to_right(expression))
