

def first(num_list1):
    num_list1.sort()
    return num_list1[0]


def last(num_list):
    num_list.sort()
    return num_list[-1]


if __name__ == '__main__':
    list_nums = [7, 9, 5]   # [ 5, 7, 9]
    print('last(list_nums)', last(list_nums))  # 9
    print('first(list_nums)', first(list_nums)) # 5

    assert last(list_nums) == 9
    assert first(list_nums) == 5
