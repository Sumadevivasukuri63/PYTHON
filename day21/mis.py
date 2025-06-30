def missing_number(nums):
    n=len(nums)
    s=n*(n+1)//2
    u=sum(nums)
    return (s-u)
input_str = input()
nums = list(map(int, input_str.strip().split()))


print( missing_number(nums))






        
        