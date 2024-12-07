# Started: 6:21pm, Ended: 7:50pm
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


# test_case2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def clean_instruction(instruction_line):
    enabled = []
    pre_enabled = instruction_line.split("do()")  # split code into enabled sections
    for partial in pre_enabled:
        # with "do" being split first, it is guaranteed that anything after
        # "don't" in each of those sections can entirely be disregarded safely
        # as such only the instruction before "don't" is stored
        enabled.append(partial.split("don't()")[0])
    return ''.join(enabled)


file = open('./memory.txt')
instructions = file.readlines()
instructions = ''.join(instructions)

todo = clean_instruction(instructions)
total = total_of_products(todo)

print(total)
