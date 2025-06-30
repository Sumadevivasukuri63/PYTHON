def duplicate(arr):
    check_num=set()
    duplicates=set()
    for item in arr:
        if item in check_num:
            duplicates.add(item)
        else:
            check_num.add(item)
    print(duplicates)
arr=[1,2,3,1,2,4]

print(duplicate(arr))





class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #return list(set(nums1)& set(nums2))
        set1=set(nums1)
        result=set()
        for num in nums2:
            if num in set1:
                result.add(num)
        return list(result)


