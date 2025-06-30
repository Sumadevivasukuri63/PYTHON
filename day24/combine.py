arr1 = [1, 2, 3, 4, 6, 7]
arr2 = [6, 7, 5, 8, 9]

result = arr1 + arr2


unique = []
for num in result:
    if num not in unique:
        unique.append(num)


n = len(unique)
for i in range(n):
    for j in range(0, n - i - 1):
        if unique[j] > unique[j + 1]:
            unique[j], unique[j + 1] = unique[j + 1], unique[j]

print(unique)






