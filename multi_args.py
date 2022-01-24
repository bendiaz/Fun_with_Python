def myarea(a,b):
    return a * b

print(myarea(4,5)) #positional
print(myarea(b=4,a=5)) #keyword

#keyword args vs non-keyword args (positional)

#don't declare one and try to pass both will cause error

#how to create a function with indefinite arguments:


###############
#non keyword arguments
def mymean(*args):
    return sum(args) / len(args)

print(mymean(1,3, 4))

def foo(*args):
    args = [x.upper() for x in args if isinstance(x, str)]
    return sorted(args)


a = 'something'   
print(foo('zebra', 313, 'apple', 'glacier', a))


def bar(**kwargs):
    return kwargs

print(bar(a=2,b=3,c=5))

def newmean(**kwargs):
    return sum(kwargs.values())/len(kwargs.values())

#keyword args return dictionaries so we must treat them as such
print(newmean(a=3,b=4))

def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)
 #.get is a dictonary-specific method for returning the value of specified key
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))