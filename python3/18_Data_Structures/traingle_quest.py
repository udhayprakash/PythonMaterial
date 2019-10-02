n = int(input('n='))
if 0 < n <= 9:
    for i in range(1, n + 1):
        print(i * (pow(10, i) // 9))

'''
input   :   9
output  :
            1
            22
            333
            4444
            55555
            666666
            7777777
            88888888
            999999999
'''
