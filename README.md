# corner_math_boggle

Brute-force Math boggle solver for 5x5 grids.  Traversal requires going from
one corner to another corner.  Solver based on enumerated paths (102,768 total)
for Self-Avoiding Walks, developed externally, see
https://stackoverflow.com/a/9172401 

The Python code traces the coordinate paths and performs left-to-right math (no
PEMDAS).

A solution is needed to filter to the correct set of solutions.  An option is
given if non-integer intermediates are not allowed.

Help shows:
```
usage: corner_math_boggle.py [-h] [--problem PROBLEM] [--no-fractions] solution

positional arguments:
  solution           Match problem against solution

optional arguments:
  -h, --help         show this help message and exit
  --problem PROBLEM  Problem file to use, default is 'problem1_5x5.txt'
  --no-fractions     Count solutions that have only integer intermediate results
```

Example for running the code:

```
python3 corner_math_boggle.py 69.0 --no-fractions
```

Output example:
```
['2', '+', '1', '*', '2', '/', '3', '*', '8', '*', '6', '*', '4', '-', '4', '/', '5', '-', '7']  3 6 2.0 16.0 96.0 384.0 380.0 76.0 69.0
['2', '+', '1', '*', '2', '/', '3', '*', '8', '*', '6', '*', '4', '-', '4', '/', '5', '-', '7']  3 6 2.0 16.0 96.0 384.0 380.0 76.0 69.0
['5', '+', '4', '*', '4', '+', '1', '+', '9', '/', '2', '*', '3']  9 36 37 46 23.0 69.0
['3', '*', '8', '*', '6', '*', '2', '/', '9', '+', '1', '*', '4', '-', '4', '/', '2', '+', '5']  24 144 288 32.0 33.0 132.0 128.0 64.0 69.0
['3', '*', '2', '*', '5', '*', '2', '/', '6', '*', '1', '+', '2', '+', '4', '*', '4', '+', '5']  6 30 60 10.0 10.0 12.0 16.0 64.0 69.0
['3', '*', '2', '*', '6', '*', '1', '+', '4', '*', '4', '/', '5', '*', '2', '+', '5']  6 36 36 40 160 32.0 64.0 69.0
['2', '+', '4', '*', '1', '+', '9', '/', '3', '*', '8', '-', '5', '*', '2', '+', '4', '-', '5']  6 6 15 5.0 40.0 35.0 70.0 74.0 69.0
['2', '+', '4', '*', '1', '*', '9', '/', '2', '*', '5', '-', '7', '*', '2', '/', '4', '+', '5']  6 6 54 27.0 135.0 128.0 256.0 64.0 69.0
['2', '+', '9', '*', '2', '*', '6', '/', '2', '+', '4', '*', '1', '+', '4', '-', '5']  11 22 132 66.0 70.0 70.0 74.0 69.0
['3', '*', '8', '*', '6', '*', '2', '/', '9', '+', '1', '*', '4', '/', '2', '+', '5', '-', '4', '+', '2']  24 144 288 32.0 33.0 132.0 66.0 71.0 67.0 69.0
['7', '-', '5', '*', '8', '*', '2', '*', '1', '*', '4', '/', '2', '+', '5']  2 16 32 32 128 64.0 69.0
['7', '-', '5', '*', '6', '*', '1', '+', '4', '*', '4', '+', '5']  2 12 12 16 64 69
['7', '*', '5', '*', '2', '*', '1', '+', '4', '-', '5']  35 70 70 74 69
['7', '-', '5', '*', '2', '+', '5', '-', '4', '*', '4', '+', '2', '+', '1', '*', '9', '/', '3']  2 4 9 5 20 22 23 207 69.0
['7', '-', '5', '/', '2', '+', '4', '*', '4', '+', '2', '+', '1', '*', '9', '/', '3']  2 1.0 5.0 20.0 22.0 23.0 207.0 69.0
15 solutions found.
```

