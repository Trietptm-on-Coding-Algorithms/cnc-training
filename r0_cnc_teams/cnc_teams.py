import sys

name_list = []
team_count = 0

def check_name_list(names):
    global name_list
    global team_count
    for name in names:
        if name == '&':
            continue
        if name in name_list:
            return
    
    for name in names:
        if name == '&':
            continue
        name_list.append(name)
    team_count += 1

line_count = None
i = 0
for line in sys.stdin:
    line = line[:-1]
    if i == line_count:
        break

    if not line_count:
        line_count = int(line)
        continue

    strs = [x.strip() for x in line.split('&')]
    check_name_list(strs)
    i += 1

print("{0} Teams".format(team_count))
