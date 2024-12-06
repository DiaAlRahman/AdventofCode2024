# Started: 7:06, Ended: 10:02
# Part 1

file = open('./reports.txt', 'r')
reports = file.readlines()

reportsArr = []
for report in reports:
    reportsArr.append([int(x) for x in report.split()])


def check_turbulence(arr):
    i, j, n = 0, 1, len(arr)
    gt, lt = 0, 0
    while j < n:
        if arr[j] > arr[i]:
            gt += 1
        elif arr[j] < arr[i]:
            lt += 1
        i, j = i + 1, j + 1
    return True if min(gt, lt) == 0 else False


def check_range(arr):
    i, j, n = 0, 1, len(arr)
    while j < n:
        if not arr[i] + 1 <= arr[j] <= arr[i] + 3 and not arr[i] - 3 <= arr[j] <= arr[i] - 1:
            return False
        i, j = i + 1, j + 1
    return True


valid_reports1 = 0
valid_reports2 = 0
for report in reportsArr:
    if check_turbulence(report) and check_range(report):
        valid_reports1 += 1

    valid = False
    for i, level in enumerate(report):
        new_report = report[:i] + report[i + 1:]
        if check_turbulence(new_report) and check_range(new_report):
            valid = True
    if valid:
        valid_reports2 += 1


print(valid_reports1, valid_reports2)

# Spent more time to find an optimal solution, essentially a way to skip checking the array by removing one element at
# a time. Regardless, I thought of the correct solution but thought it would be 'too' brute force, but it gives
# the accurate output. Which brings me to the conclusion, that I was trying to optimize for no reason.

# But anyway, the general idea is to check for turbulence (check that the array is either strictly increasing or
# decreasing) and then check for the range between each level. This itself is enough to validate a report.
# For part 2, I simply checked the arrays in the absence of each element.

# I believe I achieve a time complexity of O(l * r), where l is the maximum number of levels, and r is the number of
# reports.

