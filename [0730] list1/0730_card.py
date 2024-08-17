def counting_card(card):
    count = [0] * 10
    for num in card:
        count[num] += 1

    max_count = count[0]
    for i in range(len(count)):
        if count[i] >= max_count:
            max_count = count[i]
            max_card = i
            # max_count = count[i]
    return max_card, max_count

T = int(input())

for tc in range(T):
    n = int(input())
    data = str(input())
    card = []
    for i in range(n):
        card.append(int(data[i]))
    max_card, max_count = counting_card(card)
    print(f'#{tc+1} {max_card} {max_count}')

