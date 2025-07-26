list=[1,2,3,5]
n=len(list)
k=0
for i in range(0,n-1):
    if list[i]>list[i+1]:
        k=i
#arr=[0]*n       
for i in range(0,n-1):
    if list[(i+(n-k))%n]==list[i]:
        print(list)


for i in range(0,n-1):
    if list[i]<list[i+1]:
        print(True)
        break
    else:
        print(False)



# lst = [1, 2, 3, 0, 5]
# n = len(lst)


# k = 0
# for i in range(n - 1):
#     if lst[i] > lst[i + 1]:
#         k = i + 1
#         break


# rotated = lst[k:] + lst[:k]
# is_sorted = all(rotated[i] <= rotated[i + 1] for i in range(n - 1))

# print( is_sorted)