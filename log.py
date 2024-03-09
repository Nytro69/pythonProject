
def find(list, item):
    return find_rec(list, item, 0, len(list) - 1)

def find_rec(list, item, i, j):
    if j < i:
        return -1

    new_list = (i + j) // 2

    if list[new_list] == item:
        return new_list

    if j == i:
        return -1

    if list[new_list] < item:

        return find_rec(list, item, new_list + 1, j)

    if list[new_list] > item:

        return find_rec(list, item, i, new_list - 1)


l = [1, 4, 6, 8, 9, 10]
print(find(l, 0))