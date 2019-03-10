data = list(range(-100,100000, 3)) 
data_length = len(data)
# for index, number in enumerate(data): 
#     # print( '\r{} of {} completed'.format(index,data_length), end = '')
#     print( '\r{0:.3f} completed'.format((100 *index)/data_length), end = '')

values = {
    0: '|',
    1: '/',
    2: '-',
    3: '\\'
}
# for index, _ in enumerate(data):
#     print('\r',values.get(index%4), end=' ')

for index, _ in enumerate(data):
    print('\r', '#' * int(10*index/data_length), end = ' ')