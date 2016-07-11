import sys

def get_encrypted_idx(in_idx):
    out_idx = in_idx - 3
    if out_idx < 0:
        diff = out_idx + 26
        return diff
    return out_idx

def encrypt_char(c):
    alpha_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    i = 0
    for ac in alpha_list:
        if ac == c:
            ac_idx = get_encrypted_idx(i)
            return alpha_list[ac_idx]
        i += 1

def encrypt_sentence(sentence):
    chars = list(sentence)
    i = 0
    for c in chars:
        if c.isalpha() == True:
            chars[i] = encrypt_char(c)
        i += 1
    return str.join("", chars)

for line in sys.stdin:
    line = line.strip()
    encrypted = encrypt_sentence(line)
    print(encrypted)
