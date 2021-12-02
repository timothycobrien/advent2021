import os

with open(os.path.join(os.getcwd(), 'i', 'i2.txt'), 'r') as f:
    lines = f.readlines()

depth = 0
horizontal = 0
for l in lines:
    dir, val = l.split(' ')
    val = int(val)
    if (dir in ['down', 'up']):
        if dir == 'up':
            val *= -1
        depth += val
    else:
        horizontal += val

print('p1 - h : {} - d : {} - h*d: {}'.format(horizontal, depth, horizontal * depth))


aim = depth = horizontal = 0
for l in lines:
    dir, val = l.split(' ')
    val = int(val)
    if (dir == 'forward'):
        horizontal += val
        depth += (aim * val)
    else:
        if (dir == 'up'):
            val *= -1
        aim += val

print('p2 - h : {} - d : {} - a : {} - h*d : {}'.format(horizontal, depth, aim, horizontal * depth))
