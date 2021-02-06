alpha_len = 26

message = input("Please insert a message: ")

while True:
    try:
        key = int(input("Please enter the key number between 1 - 26: "))
        if key > 26:
            print("You didn't entered a number between 1 - 26, please try again")
            continue
        break
    except ValueError:
        print("You didn't enter a number")
    except:
        print("And error occurred")

translated = ""

for symbol in message:

    if symbol.isalpha():
        num = ord(symbol)
        num += key

        if symbol.isupper():
            if num > ord('Z'):
                num -= 26
            elif num < ord('A'):
                num += 26
        elif symbol.islower():
            if num > ord('z'):
                num -= 26
            elif num < ord('a'):
                num += 26
        translated += chr(num)
    else:
        translated += symbol
print(translated)

