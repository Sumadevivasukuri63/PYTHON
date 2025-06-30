def rotate(arr,k):
    k=k%len(arr)
    return arr[-k:]+arr[:-k]

arr=[1,2,3,4,5]
k=2
rotated=rotate(arr,k)
print(rotated)