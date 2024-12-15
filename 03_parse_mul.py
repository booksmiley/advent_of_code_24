import re


def parse(s):
    s = s.replace('mul(', '').replace(')', '')
    a, b = [float(n) for n in s.split(',')]
    return a * b


s = ''
with open('./input_03.txt', 'r') as f:
    for line in f:
        s += line.strip()

sum = 0
while True:
    green_light = re.search(r'do\(\)', s)
    red_light = re.search(r'don\'t\(\)', s)
    x = re.search(r'mul\(\d+,\d+\)', s)

    green_light_pos = green_light.start() if green_light else len(s) + 1
    red_light_pos = red_light.start() if red_light else len(s) + 1
    x_pos = x.start() if x else None
    if not x:
        break

    if x_pos < green_light_pos and x_pos < red_light_pos:
        sum += parse(x.group())
        s = s[x.end():]
    elif green_light_pos < x_pos and (red_light_pos < green_light_pos or red_light_pos > x_pos):
        sum += parse(x.group())
        s = s[x.end():]
    elif red_light_pos < x_pos and (green_light_pos < red_light_pos or green_light_pos > x_pos):
        if green_light_pos < red_light_pos:
            s = s[green_light.end():]
        else:
            s = s[green_light.start():] if green_light else ''

print(sum)