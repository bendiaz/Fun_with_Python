temps = [211, 234, 350, 324, -9999]

new_temps = [temp/10 for temp in temps]

print(new_temps)

new_temps = [temp / 10 for temp in temps if temp != -9999]

print(new_temps)

#can use list comp in functions too!

#here we check if list are numbers
def only_num(data):
    return [x for x in data if isinstance(x, int)]
        
#here we check if it's positive values
def only_pos(data):
    return [x for x in data if x>0]


new_temps = [temp/10 if temp !=-9999 else 0 for temp in temps]
print(new_temps)

#this replaces other data for 0s instead
def zeros_instead(data):
    return [x if isinstance(x,int) else 0 for x in data]

    
def convert_and_sum(data):
    return sum([float(x) for x in data])

