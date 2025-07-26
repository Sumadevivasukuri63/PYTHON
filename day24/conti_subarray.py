
def checkSubarraySum(nums, k):
    remainder_map = {0: -1}
    total = 0
    for i, num in enumerate(nums):
        total += num
        remainder = total % k if k != 0 else total

        if remainder in remainder_map:
            if i - remainder_map[remainder] > 1:
                return True
        else:
            remainder_map[remainder] = i  # Update only if not already present

    return False
nums=[23,2,6,4,7]
k=13
print(checkSubarraySum(nums,k))        