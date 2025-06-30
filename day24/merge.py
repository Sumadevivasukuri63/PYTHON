nums1=[1,2,3,4,] 
nums2=[5,6,7,8,9]
result=[]
x=y=0
n=len(nums1)
m=len(nums2)
while x<n and y<m:
    if nums1[x]<nums2[y]:
        result.append(nums1[x])
        x=+1
    else:
        result.append(nums2[y])
        y=+1
while x<n:
    result.append(nums1)
while y<m:
    result.append(nums2)
