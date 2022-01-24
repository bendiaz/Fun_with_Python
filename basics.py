monday_temps = [9.1, 8.8, 7.5, 6.6, 9.9]

# monday_temps[0][2]

student_grades = {"Mary": 91.2, "Sam": 88.8, "Johnny": 75.6}
#cannot use list slices but must use the keys

msg = "Hello World"
student_grades['Sam']

print(msg)



def mymean(value):
    if type(value) == dict:
        #can also use isinstance(value, dict)
        the_mean = sum(value.values()) /len(value)
    else:
        the_mean = sum(value) /len(value)
    return the_mean

# print("my mean:" , mymean([1,4,6]),type(sum) )


x = 1
y = 2

if x == 1 and y ==2: 
    print("yes")
else:
    print("no")

if x == 1 or y ==2:
    print("foo")
else:
    print("bar")

print(mymean(student_grades))
print(mymean(monday_temps))


##exercise - user input let's convert
def temp_check(temp):
    if temp > 25:
        return "Hot"
    elif 15 < temp < 25:
        return "Warm"
    else:
        return "Cold"

user_input = float(input("enter temperature:"))
print(temp_check(user_input))


user_input2 = input("Enter your name:")
last_name = input("Enter your last name:")
message = "Hello %s %s!" % (user_input2, last_name) #% will replace by user_input2 and need 2 %s to use both args
print(message)
#%s in use before python 3.5
#f strings not until 3.6
user_input3 = input("Enter your name:")
last_name_2 = input("Enter your last name again...")
message = f"Hello, again {user_input3} {last_name_2}" #more robust/ conventional
print(message)


### exercise

#kinda dumb since I can't pass inputs into the function

def talking_guy(person):
    msg = "Hi %s" % (person).capitalize()
    return msg
person = input("enter name please: ")
result = talking_guy(person) #needed to assign to function after it was defined
print(result)


#for loop time! :)

#dir(__builtins__) to find built in functions

for tempss in monday_temps:
    print(round(tempss))