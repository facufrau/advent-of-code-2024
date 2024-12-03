# --- Day 3: Mull It Over ---
import re

with open("input03.txt") as file:
    content = file.read()

# Part one
pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
iterator = pattern.finditer(content)
total_1 = 0
for match in iterator:
    mult_tpl = eval(match.group()[3:])
    result = mult_tpl[0] * mult_tpl[1]
    total_1 += result

print(f"Part one answer -->  {total_1}")

# Part two 
pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)")
iterator = pattern.finditer(content)
total_2 = 0
do = True
for match in iterator:
    command = match.group()
    if "do()" in command:
        do = True
    elif "don't()" in command:
        do = False
    elif do:
        mult_tpl = eval(match.group()[3:])
        result = mult_tpl[0] * mult_tpl[1]
        total_2 += result

print(f"Part two answer -->  {total_2}")
