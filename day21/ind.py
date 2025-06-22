nums=list(map(int,input().split()))
target=0
dict={}
for i,num in enumerate(nums):
    s=target-num
    if s in dict:
        return dict[s],i
dict[num]=i
        
        # if target==nums[0]+nums[1]:
        #     return [0,1]
        # elif target==nums[0]+nums[2]:
        #     return [0,2]
        # else:
        #     return [1,2]  


        