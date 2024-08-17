T = int(input())
for tc in range(1, T+1):
    s = list(input())
    i =0
    while i < len(s)-1:
        if s[i] == s[i+1]:
            s.pop(i)
            # print(1, s)
            s.pop(i)
            # print(2, s)
            i = 0
        # if s[i] == s[i-1]:
        #     s.pop(i-1)
        #     s.pop(i-1)
            # i -= 1
        else: 
            i += 1
            # print(3, s)
    print(f'#{tc}', len(s))