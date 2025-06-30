def findMaxAverage(nums, k):
    max_average=0
   
    current_sum = sum(nums[:k])
    max_sum = current_sum
    
  
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)
        max_average= max_sum / k
        return max_average

nums=[1, 12, -5 ,-6, 50, 3]
k=4
print(findMaxAverage(nums,k))
