def missing_number(nums: list[int]) -> int:
    n=len(nums)
    s=n*(n+1)//2
    u=sum(nums)
    return (s-u)
input_str = input()
nums = list(map(int, input_str.strip().split()))


print("The missing number is:", missing_number(nums))

        
        