l1 = [1, 2, 3,4]
l2 = [4, 5, 6, 7]

l1_s = [x ** 0.5 for x in l1]
l2_s = [x ** 0.5 for x in l2]


def same_list(l1, l2):
    if not l1 or not l2:
        return False
    else:
        return l1_s == l2 or l2_s == l1


same_list(l1, l2)