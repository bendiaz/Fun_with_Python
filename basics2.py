monday_temps = [9.1, 8.8, 7.5, 6.6, 9.9]

for temps in monday_temps:
    print(round(temps))
    print("next")
print("finished")

for letter in "hello":
    print(letter.title())


# print if larger than 50
colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    if color >50:
        print(color)

#print if integer

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if type(color) == int:
        print(color)


## now if color is both an int and bigger than 50
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if type(color) == int and color >50:
        print(color)

## looping through dictionaries

student_grades = {"Mary": 91.2, "Sam": 88.8, "Johnny": 75.6}

for grades in student_grades.items():
    print(grades)

for grades in student_grades.keys():
    print(grades)

for grades in student_grades.values():
    print(grades)


## we can combine dict loop with string formatting to create text containing info from
#dict itself

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))

    #calls using indexing

#####   an even simplier way to do this  #######


 
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))

    #calls using location (i assume)


#returning the numbers

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for first_thing, second_thing in phone_numbers.items():
    print("%s: %s" % (first_thing, second_thing))


phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
#replace + with 00
for something in phone_numbers.values():
    print(something.replace("+", "00"))


##while loops

username = ''
# will continue to prompt until the username is pypy thus ending the code 
#while username is NOT equal to pypy run this code...
while username != "pypy":
    username = input("Enter username: ")


