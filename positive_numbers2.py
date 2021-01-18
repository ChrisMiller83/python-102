
list1 = [-2, 5, -12, 20, 30, 13, 200, -69, 83]
list2 = [3, -1, -20, 21, 33, 101, 24, 39, 41]
combo_list = list1 + list2


for num in combo_list:
    if num > 0:
        combo_list.sort()
        print(num, end = ", ")