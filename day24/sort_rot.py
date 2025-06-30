def rotate_number(nums):
        count=0      #counts the number of times if condtion files
        n=len(nums)
        for i in range(0,n):
            if nums[i]>nums[(i+1)%n]:
                count+=1
                if count>1:
                    return False
        return True

nums=[3,2,5,1,4]

print(rotate_number(nums))