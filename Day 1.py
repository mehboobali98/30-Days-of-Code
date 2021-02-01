i = 4
d = 4.0
s = 'HackerRank '

import fileinput

# Declare second integer, double, and String variables.
_i = int()
_d = float()
_s = str()
# Read and save an integer, double, and String to your variables.
lines = fileinput.input()

_i = int(lines[0])
_d = float(lines[1])
_s = lines[2]

# Print the sum of both integer variables on a new line.
print(i + _i)
# Print the sum of the double variables on a new line.
print(d + _d)
# Concatenate and print the String variables on a new line
print(s + _s)
# The 's' variable above should be printed first.