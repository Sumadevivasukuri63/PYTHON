def is_palindrome(s):
    suma= s==s[::-1]
    return suma


name=input("Enter a name:")
if is_palindrome(name):
    print("It is palindrome")
else:
    print("It is not a palindrome")

    