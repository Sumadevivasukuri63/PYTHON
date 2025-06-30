# list=[3,5,0,6,0,4,8,0]
# result=[]
# for i in range(len(list)):
#     if list[i]!=0:
#         result.append(list[i])
# zeros=list.count(0)
# for i in range(zeros):
#     result.append(0)
# print(result)




def moveZeroes( nums):
        index=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[index]=nums[i]
                index+=1
        for i in range(index,len(nums)):
            nums[i]=0
nums = [0, 1, 0, 3, 1]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
        
    