import re

with open('out', 'r') as f:
    count = 0.0
    lines = 0

    for line in f:
        matched = re.search(r'([0-9]+)', line)
        if matched:
            count += len(matched.groups()[0])
            lines += 1
    print count/lines
