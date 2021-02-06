string = input("Please enter an word: ")

secret_string = ""

for char in string:
    print(ord(char))
    secret_string += str(ord(char) - 23)

print(secret_string)

n = 2

string = ""

for i in range(0, len(secret_string)-1, 2):
    char_code = secret_string[i] + secret_string[i+1]
    string += chr(int(char_code) + 23)

print("Original: ", string)