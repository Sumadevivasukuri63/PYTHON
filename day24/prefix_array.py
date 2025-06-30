arr=[-1 ,-1, 2, -2, 4 ,-1,8]
target= 3
sum = 0
longest = 0
prefix_sum = {}
for num in range(0 , len(arr)):
    sum +=arr[num]
    if sum == target:
        longest = num +1
    else:
        if (sum - target) in prefix_sum:
            longest = max(longest, num-prefix_sum[sum-target])
    prefix_sum[sum] = num
print(arr)
print(longest)