import sys

def check_pal(val):
    digits = list(val)
    digcnt = len(digits)
    i = 0
    for digit in digits:
        if i == digcnt:
            break
        if i == 0:
            if digit != digits[digcnt - 1]:
                return False
        else:
            if digit != digits[(i * -1) - 1]:
                return False
        i += 1
    return True

for line in sys.stdin:
    line = line.strip()
    if line == '#':
        break

    lineint = int(line)
    binstr = bin(lineint)[2:]
    bincheck = check_pal(binstr)
    hexstr = hex(lineint)[2:]
    hexcheck = check_pal(hexstr)
    if bincheck == False or hexcheck == False:
        print("{0} is NOT a binhex palindrome ({1},{2})".format(lineint, binstr, hexstr))
    else:
        print("{0} is a binhex palindrome ({1},{2})".format(lineint, binstr, hexstr))
