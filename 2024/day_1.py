with open('2024/input_1.txt', 'r') as f:
    #Part 1
    lst_1, lst_2 = list(), list()
    for line in f:
        lst_1_item, lst_2_item = line.split()
        lst_1.append(int(lst_1_item))
        lst_2.append(int(lst_2_item))
    
    lst_1.sort()
    lst_2.sort()
    tot_d = 0
    for i in range(len(lst_1)):
        tot_d += abs(lst_1[i] - lst_2[i])
    print(tot_d)

    #################################
    #Part 2
    lst_2_dic = {}
    for item in lst_2:
        if item in lst_2_dic:
            lst_2_dic[item] += 1
        else:
            lst_2_dic[item] = 1
    
    total_s = 0
    for item in lst_1:
        if item in lst_2:
            total_s += item * lst_2_dic[item]
    print(total_s)