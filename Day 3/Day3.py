# Started: 6:21pm
import re

# Test cases that allowed me to learn the mechanics of the functions in the 'regex' docs of Python

# test_case = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
# pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
# matches = re.findall()
# print(matches)
# total = 0
# for x,y in matches:
#     total += (int(x) * int(y))
# print(total)

patter_without_capturing_groups = r"mul\(\d{1,3},\d{1,3}\)"
# The capturing groups allow findAll to cleanly return a list of the required tuples.


def total_of_products(instruction_line):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, instruction_line)
    total = 0
    for x,y in matches:
        total += (int(x) * int(y))
    return total


file = open('./memory.txt')
instructions = file.readlines()

final_total = 0
for instruction in instructions:
    final_total += total_of_products(instruction)

print(final_total)

