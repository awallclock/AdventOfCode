# read file
# split file into 2 arrays using spaces as delimiters
# sort each array, low to high
# subtract right from left, absolute
# add difference together
# output difference
filename = "input"

with open(filename) as f:
    content = f.read().splitlines()
left_array = []
right_array = []
sum = 0
for line in content:
    split_line = line.split()
    left_array.append(split_line[0])
    right_array.append(split_line[1])

for left_num in range(0, len(left_array)):
    count = 0
    for right_num in range(0, len(right_array)):
        if int(left_array[left_num]) == int(right_array[right_num]):
            count += 1
    sum += count * (int(left_array[left_num]))
print(sum)

