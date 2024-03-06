def merge_sort(list):

    if len(list) <= 1:
        return list

    m = len(list) // 2

    list1 = merge_sort(list[:m])

    list2 = merge_sort(list[m:])

    return merge(list1, list2)



def merge(l1, l2):
    c1 = 0
    c2 = 0
    final = []

    while c1 < len(l1) and c2 < len(l2):

        if l1[c1] < l2[c2]:
            final.append(l1[c1])
            c1 += 1

        else:
            final.append(l2[c2])
            c2 += 1

    while c1 < len(l1):
        final.append(l1[c1])
        c1 += 1

    while c2 < len(l2):
        final.append(l2[c2])
        c2 += 1

    return final


list3 = [1, 9, 7, 10, 16, 4, 15, 11, 19, 13, 14, 2, 12, 18, 20, 5, 17, 6, 8, 3]

print(merge_sort(list3))