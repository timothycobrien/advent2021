import os

with open(os.path.join(os.getcwd(), 'i', 'i3.txt'), 'r') as f:
    lines = f.readlines()

count_arr = (len(lines[0]) - 1) * [0]
for line in lines:
    for i, c in enumerate(line):
        if c == '\n':
            continue
        count_arr[i] += int(c)

length = len(lines)/2
gamma = ""
epsilon = ""
for v in count_arr:
    if v > length:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(count_arr)

def bin_to_dec(binary):
    res = 0
    for c in binary:
        res <<= 1
        res += int(c)
    return res

gamma_dec = bin_to_dec(gamma)
epsilon_dec = bin_to_dec(epsilon)

print("{} : {} : {} : {} : {}".format( gamma, gamma_dec, epsilon, epsilon_dec, gamma_dec * epsilon_dec))

ox = lines.copy()
co = lines.copy()

def most_common_bit(arr, index):
    count = 0
    for l in arr:
        count += int(l[index])
    target = len(arr) / 2
    if count == target:
        return '1'
    elif count > target:
        return '1'
    else:
        return '0'

def process_string(arr, flag=True):
    i = -1
    while len(arr) > 1:
        i += 1
        mcb = most_common_bit(arr, i)
        if not flag:
            mcb = '1' if mcb == '0' else '0'
        arr = list(filter(lambda l: l[i] == mcb, arr))
    return arr[0]

ox = process_string(ox, True)
co = process_string(co, False)

ox = ox[:-1]
co = co[:-1]

print(ox, co)

ox_dec = bin_to_dec(ox)
co_dec = bin_to_dec(co)

print(("{} : {} : {} : {} : {}".format( ox, ox_dec, co, co_dec, ox_dec * co_dec)))


