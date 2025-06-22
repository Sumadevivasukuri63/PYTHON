T =int(input())

for i in range(T):
    N = int(input())  
    count = {}

    for j in range(N):
        doll = int(input())
        if doll in count:
            count[doll] += 1
        else:
            count[doll] = 1

    
    for doll_type, freq in count.items():
        if freq % 2 != 0:
            print(doll_type)
            break

            