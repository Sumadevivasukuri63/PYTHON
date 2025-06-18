def valid_email(mail):
    if '@' in mail and '.' in mail:
        return True
    else:
        return False


email=input()  
mail=email[1:len(email)-1] 
print(mail)
print(valid_email(mail))     
