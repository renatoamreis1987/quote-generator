samp_string = "   This is a very important string  "

samp_string = samp_string.lstrip()
samp_string = samp_string.rstrip()

print("Uppercase : ", samp_string.upper())
print("Lowercase : ", samp_string.lower())

samp_string_split = samp_string.split()

for string in samp_string_split:
    print(string)

print(len(samp_string))

samp_string = samp_string.replace("very ", "kind of ")
print(samp_string)

string_z = "z"

print(string_z.isalpha())
print(string_z.isnumeric())
print(string_z.isspace())