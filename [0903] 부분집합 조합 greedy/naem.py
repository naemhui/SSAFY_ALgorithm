arr = ['O','X']
path = []
name = ['A', 'B', 'C']

def print_name():
    for i in range(3):
        if path[i] == 'O':
            print(name[i], end=' ')
            # print()



def run(lev):
    if lev == 3:
        print_name()
        return
    
    for i in range(2):
        path.append(arr[i])
        run(lev+1)
        print()
        print('pop 전: ', path)
        path.pop()
        print('pop 후: ', path)
        print()

run(0)