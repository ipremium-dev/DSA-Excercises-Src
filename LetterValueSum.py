ALPHABET = "abcdefghijklmnopqrstuvwxyz"  # constant


def pull_char_val(c):  # Pass the Character Letter from a - z
    if c.isalpha(): # isalpha check if a character belong to Alphabet
        for ctr in range(len(ALPHABET)):
            #print(ALPHABET[ctr] + " = " + str(ctr + 1))
            if ALPHABET[ctr] == c.casefold():  #use casfold to always convert to lower case
                return ctr + 1
    else:
        return 0


inputChar = input("Enter Series of Letter: ")

print("You Entered " + str(inputChar))
sum = 0
for ctr in range(len(inputChar)):
    print(inputChar[ctr] + " = " + str(pull_char_val(inputChar[ctr])))
    sum += pull_char_val(inputChar[ctr])
print("Lettervaluesum: " + str(sum))
