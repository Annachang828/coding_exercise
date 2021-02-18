# 我自己的解答
def find_max(a_list):
    if not a_list:
        return 0
    else:
        return max(a_list)

print(find_max([1, 2, 3]))


# 老師的解答
def find_max(a_list):
    if not a_list:
        return 0
    max_num = a_list[0]
    for num in a_list:
        if num > max_num:
            max_num = num
    return max_num

print(find_max([1, 2, 3]))