import os

with open(os.path.join(os.getcwd(), 'i', 'i1.txt'), 'r') as f:
    lines = f.readlines()

count = 0
prev = int(lines[0])
for l in lines[1:]:
    cur = int(l)
    if (cur > prev):
        count += 1
    prev = cur
print('p1', count)

count = 0
old_sliding = int(lines[0]) + int(lines[1]) + int(lines[2])
for i, l in enumerate(lines[3:]):
    cur = old_sliding + int(l) - int(lines[i])
    if cur > old_sliding:
        count +=1
    old_sliding = cur
print('p2', count)