def move_zeros(array):
    return [x for x in array if x != 0] + [z for z in array if z == 0]


print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))