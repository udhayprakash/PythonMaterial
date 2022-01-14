def flatten_list(mylist, flatlist=None):
    if not flatlist:
        flatlist = []

    for ele in mylist:
        if isinstance(ele, list):
            flatlist.extend(flatten_list(ele))
        else:
            flatlist.append(ele)
    return flatlist


print(flatten_list([1, 2, 3]))
print(flatten_list([1, 2, [3]]))
print(flatten_list([1, [2], [3]]))
print(flatten_list([[1], [2], [3]]))
print(flatten_list([[1], [2], [3]]))
print(flatten_list([[1], [2], [[3]]]))
print(flatten_list([[1], [2], [[[[[3]]]]]]))
