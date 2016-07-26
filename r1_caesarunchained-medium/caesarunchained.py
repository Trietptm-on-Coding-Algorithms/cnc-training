import sys

def get_normal_idx(in_idx):
    out_idx = in_idx - 3
    if out_idx < 0:
        diff = out_idx + 26
        return diff
    return out_idx

def get_rolling_idx(curr_idx, last_idx):
    roll_idx = curr_idx + last_idx
    if roll_idx > 26:
        roll_idx = roll_idx - 26
    return roll_idx

def ceaser_encrypt_char(c):
    alpha_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    i = 0
    for ac in alpha_list:
        if ac == c:
            ac_idx = get_normal_idx(i)
            return (ac_idx, alpha_list[ac_idx])
        i += 1

def rolling_encrypt_char(c, idx):
    alpha_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    i = 0
    for ac in alpha_list:        
        if ac == c:
            ac_idx = get_rolling_idx(i, idx)
            return (ac_idx, alpha_list[ac_idx])
        i += 1
    
def encrypt_sentence(sentence):
    chars = list(sentence)
    i = 0
    idx = -1
    for c in chars:
        # first character encrypt and get idx
        if c.isalpha() == True and idx = -1:
            idx, chars[i] = ceaser_encrypt_char(c)

        # non-first character roll encryption
        if c.isalpha() == True and idx != -1:
            idx, chars[i] = rolling_encrypt_char(c, idx)

        i += 1
    return str.join("", chars)

for line in sys.stdin:
    line = line.strip()
    encrypted = encrypt_sentence(line)
    print(encrypted)
