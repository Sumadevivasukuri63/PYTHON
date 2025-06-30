def consecutive(nums):
    max_count=count=0
    for num in nums:
        if num==1:
            count+=1
            max_count=max(max_count,count)
        else:
            count=0
    print(max_count)
nums=[1,1 ,2,1,3,1,1,1]
print(consecutive(nums))