inputChar = input("Enter number: ")

if str(inputChar).isnumeric() == True:
    print("Even" if int(inputChar) % 2 == 0 else "Odd")
else:
    print("Please enter numeric number")