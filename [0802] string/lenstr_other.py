########
T = int(input())
 
for t in range(T):
    str1 = input()
    str1_dict = {}
    for i in str1:
        str1_dict.setdefault(i, 0)
    keys1 = list(str1_dict.keys())
    str2 = input()
    for i in str2:
        if i in keys1:
            str1_dict[i] += 1
 
    print(f"#{t+1} {max(str1_dict.values())}")

########
t = int(input())
 
for tc in range(1, t+1):
    str1 = input()
    str2 = input()
    max_num = 0
 
    for i in str1:
        count = 0
        for j in str2:
            if i == j:
                count += 1
 
        if max_num < count:
            max_num = count
 
    print(f'#{tc} {max_num}')