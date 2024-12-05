import sys
sys.setrecursionlimit(5000)

def ordered(rules, page, i = 0, before = []):
    if i < len(page):
        num = page[i]
        if before == []:
            return ordered(rules, page, i + 1, [num])
        for j, prev in enumerate(before):
            if [num, prev] in rules:
                # return 0   # returns 7365
                before.append(prev)
                before[j] = num
                page = before + page[i+1:]
                return ordered(rules, page)
        before.append(num)
        return ordered(rules, page, i + 1, before)
    return page[len(page) // 2]

with open('2024/input_5.txt', 'r') as f:
    rules, pages = [], []
    for line in f:
        line = line.strip('\n')
        if '|' in line:
            rules.append([int(x) for x in line.split('|')])
        elif (line != ''):
            pages.append([int(x) for x in line.split(',')])
    s = 0
    for page in pages:
        s += ordered(rules, page) 
    print(s)