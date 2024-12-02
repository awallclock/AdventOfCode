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
left_array.sort()
right_array.sort()

for num in range(0, len(left_array)):
    print(f"Left array number: {left_array[num]}")
    print(f"Right array number: {right_array[num]}")
    
    sum += abs(int(left_array[num]) - int(right_array[num]))
print(sum)
