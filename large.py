x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
z=int(input("enter the value of z:"))
if (x>=y) and (x>=z):
    print("the largest value is:",x)
elif(y>=x) and (y>=z):
    print("the largest value is:",y)
else:
    print("the largest value is:",z)
