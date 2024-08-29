#!/usr/bin/env python3
#
# Complete solver for 5x5 math boggle-style problem.
# Constructs all solutions from any corner to another corner.
# Uses solved coordinate paths developed from self-avoiding walks
#

import numpy as np
import argparse
from numpy import genfromtxt 
parser = argparse.ArgumentParser()
parser.add_argument("solution", help="Match problem against solution", type=float)
parser.add_argument("--problem", help="Problem file to use, default is 'problem1_5x5.txt'", default="problem1_5x5.txt", type=str)
parser.add_argument("--no-fractions", help="Count solutions that have only integer intermediate results",
                    action="store_true")
args = parser.parse_args()


def is_frac(n):
    numeric_types = (int, float)
    assert isinstance(n, numeric_types), 'n must be numeric :/'
    if type(n) is int: return False
    return n != float(int(n))


def do_math_left_to_right(expression):
    """"Perform math operations on strings going from left to right. Untested with double digits."""
    digits = "0123456789"
    pieces = []
    fractional = False

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
        if is_frac(result):
            fractional = True
        intermediates += " " + str(result)
        last_piece = str(result)
    return intermediates, fractional, result


problem_flip = genfromtxt(args.problem, dtype='str', delimiter=' ')
# reverse all the rows, to interpret the bottom left corner as (0, 0)
problem = problem_flip[::-1,:]

coord_files = [
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

solution_count = 0
for coord_file in coord_files:
    with open(coord_file, "r") as f:
        for line in f:
            expression = []

            # a solution row in a 2x2 grid might look like
            # 2. solution: 1,1,2,1,2,2
            # coordinates in files are one-based so subtract one from all elements
            # we want to have result = '0,0,1,0,1,1'

            result = line.split()[2:][0].split(",")
            result = [int(i) - 1 for i in result]
            
            # coords come in the form of 0,0,1,0,1,1
            # which we want to interpret as (0,0) to (1,0) to (1,1)
            n = 2
            coords = list(tuple(result[i : i + n]) for i in range(0, len(result), n))
            for coord in coords:
                expression.append(str(problem[coord]))

            intermediates, fractional, result = do_math_left_to_right(expression)

            if np.isclose(result, args.solution):
                if args.no_fractions:
                    if not fractional:
                        solution_count += 1
                        print(expression, intermediates)
                else:
                    solution_count += 1
                    print(expression, intermediates)

print(f"{solution_count} solutions found.")
