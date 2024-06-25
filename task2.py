a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
print("1.addition")
print("2.multiplication")
print("3.subtraction")
print("4.division")
print("5.power(a to the power b)")
print("6.remainder when divided")
print("Which operator do you want to use?")
choice = int(input("enter choice 1/2/3/4/5/6:"))
if choice == 1:
    print(a+b)
elif choice == 2:
    print(a*b)
elif choice == 3:
    print(a-b)
elif choice == 4:
    if b==0:
        print("can't be divided")
    else:
        print(a/b)
elif choice == 5:
    print(a**b)
else:
    print(a%b)