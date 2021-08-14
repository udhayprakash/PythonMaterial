def flatten(given_list, final=None):
    if not final:
        final = []
    for each_ele in given_list:
        if isinstance(each_ele, (str, int, float, None)):
            final.append(each_ele)
        elif isinstance(each_ele, (list, tuple, set, dict)):
            final.extend(each_ele)
        else:
            raise Exception(f"unhandled type:{type(each_ele)}")
    return


print(flatten([[1], [2], [3], [4], [5]]))
