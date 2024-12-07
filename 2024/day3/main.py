import re
txt = "input"

with open(txt, "r") as f:
    content = f.read()

regexed = re.findall(r"\bmul\(\d{1,3},\d{1,3}\)", content)

sum = 0
for line in regexed:
    numbers = re.findall(r"\b\d{1,3}", line)
    sum += int(numbers[0]) * int(numbers[1])
print(sum)
