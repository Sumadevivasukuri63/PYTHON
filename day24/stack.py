expression="{{{2}+{3}}}{"
suma=[]
for i in expression:
    if i=="{":
        suma.append(i)
    elif i=="}":
        suma.pop()
    
    else:
        continue
print(suma[-1])
if len(suma)==0:
    print("valid exp")
else:
    print("invalid exp")
