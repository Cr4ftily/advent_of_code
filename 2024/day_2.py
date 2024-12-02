def safe(report, dampener = 0, iod = 0, i = 0):
    if i + 1 < len(report):
        j = i + 1
        diff = report[i] - report[j]
        iod = iod if iod != 0 else diff     # increments or decrements
        if abs(diff) > 3 or diff * iod <= 0:
            if dampener:
                return max(0 if not i else safe(report[:(i-1)] + report[i:], 0), 
                           safe(report[:i] + report[j:], 0), 
                           safe(report[:j] + report[(j+1):], 0))
            else:
                return 0
    else:
        return 1
    return safe(report, dampener, iod, j) 

with open('2024/input_2.txt', 'r') as f:
    s = 0
    for line in f:
        # s += safe([int(x) for x in line.split()])
        s += safe([int(x) for x in line.split()], 1)
    print(s)