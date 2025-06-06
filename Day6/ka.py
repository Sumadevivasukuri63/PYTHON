try:
    num1=int(input("Enter a number1:"))
    num2=int(input("Enter a number2:"))
    num=num1+num2
    print(num)
except Exception as e:
    print(f"Error is {e}")
else:
    print("no error is there:")
finally:
    print("ok madam! your program is complete:")