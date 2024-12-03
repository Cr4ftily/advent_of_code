def is_int(s):
    if s == '':
        return False
    for char in s:
        if not char.isdigit():
            return False
    return True
    
def parse(dos):
        s = 0
        muls = dos.split('mul(')
        for mul in muls:
            n1, n2 = 0, 0
            nums1 = mul.split(',', 1)
            if len(nums1) > 1:
                if is_int(nums1[0]) and len(nums1[0]) < 4:
                    n1 = int(nums1[0])
            else:
                continue
            nums2 = nums1[1].split(')', 1)
            if len(nums2) > 1:
                if is_int(nums2[0]) and len(nums2[0]) < 4:
                    n2 = int(nums2[0])
            else:
                continue
            s +=  n1 * n2
            print(f"{n1} {n2}")
        return s

def sum(line):
    s = 0
    dos = []
    start = not 'don\'t()' in line[:7]
    do_donts = line.split('don\'t()')
    if start:
        s += parse(do_donts[0])
        if len(do_donts) > 1:
            do_donts = do_donts[1:]
        else:
            return s
    for donts in do_donts:
        print("dont")
        # print(donts)  
        if 'do()' in donts:
            print("do")
            dos = donts.split('do()', 1)
            s += parse(dos[1])
    return s

with open('2024/input_3.txt', 'r') as f:
    input = ''
    for line in f:
        input = input + line
    print(sum(input))