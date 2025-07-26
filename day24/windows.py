arr=[2,4,5,3,6,7,16]
k=4
n=len(arr)
window_sum=0
maximum=0
for i in range(0,k):
    window_sum += arr[i]
    maximum=window_sum

for i in range(k,n-1):
    window_sum+=arr[i]-arr[i-k]
    maximum=max(window_sum,maximum)
print(maximum)