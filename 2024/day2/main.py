input_file = 'input'
with open(input_file, 'r') as file:
    content = file.readlines()

count = 0
def find_safe(starter_line):
    line_array = list(map(int, starter_line.strip().split()))
    if not (line_array == sorted(line_array)) and not line_array == sorted(line_array,reverse=True):
        return False
    for i in range(0, len(line_array)- 1):
        if 0 < abs(line_array[i] - line_array[i+1]) < 3:
            return True

