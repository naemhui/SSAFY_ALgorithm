arr = ['A', 'B', 'C']
n = len(arr)


def get_sub(tar):
    cnt = 0  # 1의 개수 셀 수 있음
    for i in range(n):
        # == 'O' 대신 &연산으로. 메모리도 적게 차지하고 간결 굿
        if tar & 0x1:  # 0x1이나 0b1이나 1이나.. 근데 관례적으로 0x1로 적음
            print(arr[i], end='')
        tar >>= 1
    return cnt

for tar in range(0, 1 << n):  # 전체 부분집합을 확인하겠다 !!! range(0, 8)
    print('{', end='')
    get_sub(tar)
    print('}')