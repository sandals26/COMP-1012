list1 = [3, 12, 18, 23, 26, 31, 34, 40]
list2 = [5, 8, 10, 11, 18, 23, 29]
for item in list1:
    for item2 in list2:
        if item == item2:
            print("List 1 and 2 have: {} in common".format(item))