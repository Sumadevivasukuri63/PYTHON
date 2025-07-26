# def consecutive(nums):
#     max_count=count=0
#     for num in nums:
#         if num==1:
#             count+=1
#             max_count=max(max_count,count)
#         else:
#             count=0
#     print(max_count)
# nums=[1,1 ,2,1,3,1,1,1]
# print(consecutive(nums))




# Take user input as a list of integers
user_input = input("Enter numbers separated by commas (e.g., 1,2,3,4): ")
data = [int(x.strip()) for x in user_input.split(",")]

# Swap adjacent elements
for i in range(0, len(data) - 1, 2):
    data[i], data[i + 1] = data[i + 1], data[i]

# Output the result
print("Swapped list:", data)
