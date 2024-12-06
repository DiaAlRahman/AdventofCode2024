# Part 1
file = open('location_ids.txt', 'r')
location_ids = file.readlines()

left, right = [], []
for row in location_ids:
    row = row.split('   ')
    left.append(int(row[0])), right.append(int(row[1]))

left.sort(), right.sort()

i, n, total = 0, len(location_ids), 0
while i < n:
    total += abs(left[i] - right[i])
    i += 1

print(total)

# My first ever AoC participation, a bit late to the party, but this question gave me a boost of confidence.
# So, the general approach here was to dump the input in a text file, read it of line by line, and then create a
# left and right array. The arrays are sorted and the difference between the corresponding location ids are added
# to a total. It is important to note that negative distance may occur, which may result in a lower output.

########################################################################################################################

# Part 2

total_similarity = 0
for L in left:
    count = right.count(L)
    total_similarity += (L * count)
print(total_similarity)

# I was looking for the hidden trick, turns out there was none.
# Initially, I was thinking if I should/could optimize the solution, which I deemed unnecessary
# given that it's accurate anyway.
# The idea for optimization was to keep count of the appearance of the values in the left, so it wouldn't
# be required to be counted again and again in the right array.

