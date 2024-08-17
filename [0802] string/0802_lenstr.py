def max_count(str1, str2):
    dict = {}
    for alphabet in str1:
        dict[alphabet] = 0
    # 여기까지 하면 {'A':0, 'B':0, ...} 이런 식으로 만들어짐
    
    for alphabet in str2:
        for _ in dict.keys():
            if alphabet == _:
                dict[_] += 1
    # 이제 {알파벳: count} dict 만들어짐

    max_count = 0
    for count in dict.values():
        if count > max_count:
            max_count = count
    return max_count
        

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    result = max_count(str1, str2)
    print(f'#{tc} {result}')
