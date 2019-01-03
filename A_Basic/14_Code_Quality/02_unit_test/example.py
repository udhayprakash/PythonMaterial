# ch6_example.py

def first(num_list1):
    num_list1.sort()
    return num_list1[0]


def last(num_list):
    num_list.sort()
    return num_list[-1]


if __name__ == '__main__':
    list_nums = [7, 9, 5]
    print 'last(list_nums)', last(list_nums)
    print 'first(list_nums)', first(list_nums)
