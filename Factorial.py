
print("Factorial")
input_val = input("Please enter a number: ")

if input_val.isdigit() and int(input_val) > 0 :
    fact = 1
    for ctr in range(1, int(input_val) + 1):
        print(ctr)
        fact = fact * ctr
    print("Factorial of " + input_val + ": " +str(fact))
else:
    print("Please enter positive value greater than 0")