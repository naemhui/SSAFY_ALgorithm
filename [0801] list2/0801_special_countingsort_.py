T = int(input())
for tc in range(1,T+1):
    n = int(input())
    data = list(map(int, input().split()))
    my_switch = True

    for i in range(n-1):
        if my_switch:
            max_nums_index = i
            for j in range(i+1,n):
                if data[max_nums_index] < data[j]:
                    max_nums_index = j
            data[max_nums_index], data[i] =data[i], data[max_nums_index]
            my_switch = False
        else:
            min_nums_index = i
            for j in range(i+1,n):
                if data[min_nums_index] > data[j]:
                    min_nums_index = j
            data[min_nums_index], data[i] = data[i], data[min_nums_index]
            my_switch = True
    
    result = data[:10]
    print(f'#{tc}' , end=" ")
    print(*result)