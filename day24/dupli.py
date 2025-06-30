
def removeDuplicates( nums):
        if not  nums:
            return 0
        s=0
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                s+=1
                nums[s]=nums[i]
                
        return s+1

nums=[1,1,2,3,3,5]
s=removeDuplicates(nums)
print( s)
print (nums[:s])

        
        