
age = int(input("Please enter the age: "))

if age <= 5:
    print("Go to kindergarten")
elif 6 <= age <= 17:
    grade = age - 5
    print("Go to grade {}".format(grade))
else:
    print("Go to College")