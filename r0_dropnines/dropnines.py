import sys
import re

for line in sys.stdin:
    line = line.strip()
    if line == '#':
        break

    num_strs = re.split(r'[+|=]', line)
    add_digits = []
    res_digits = []
    i = 0
    last = len(num_strs) - 1
    for num_str in num_strs:
        for digit in list(num_str):
            digit = int(digit)
            if i != last:
                if digit != 9:
                    add_digits.append(digit)
            else:
                res_digits.append(digit)
        i += 1

    res1 = 0
    for digit in add_digits:
        res1 += digit

    res2 = 0
    for digit in res_digits:
        res2 += digit

    if res1 == res2:
        print("TRUE")
    else:
        print("FALSE")
