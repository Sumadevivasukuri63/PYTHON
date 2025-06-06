number = input("Enter a number: ")

# Reverse the number
reversed_number = number[::-1]

# Check if the original number and reversed number are the same
if number == reversed_number:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
