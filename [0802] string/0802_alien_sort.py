import sys
sys.stdin = open("GNS_test_input.txt", "r")

dict = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
keys = list(dict.keys())

T = int(input())
for tc in range(1, T+1):
    input_num = input()
    data = list(map(str, input().split()))

    lst = []
    for num in data:
        lst.append(dict[num])
        
    sort_lst = sorted(lst)


    alien_lst = [keys[num] for num in sort_lst]
    # alien_lst = []
    # for num in sort_lst:
    #     alien_lst.append(keys[num])
    print(f'#{tc}')
    print(*alien_lst)
    