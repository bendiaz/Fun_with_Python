#given two non-neg ints as a string, return the sum of each
#can't use built-in or convert to int directly


num1 = '324'
num2 = '8438'

#Approach 1

def solution1(num1,num2):
    eval(num1)+eval(num2)
    return str(eval(num1) + eval(num2))

print("solution 1" , solution1(num1,num2))

#approach 2
#given a string of length 1 the ord() function returns an int representing the unicode 
#code point of the character when the argument is a unicode object, or the value of the
#byte when the argument is 8-bit string

def solution2(num1, num2):
    n1, n2 = 0,0
    m1,m2 = 10**(len(num1)-1), 10**(len(num2)-1)

    for i in num1:
        n1 += (ord(i) - ord("0")) * m1
        m1 = m1//10 #floor division

    for i in num2:
        n2 += (ord(i) - ord("0")) * m2
        m2 = m2//10

    return str(n1+n2) #be careful where this return ends because it can accidently catch just 1 loop





print("solution 2", solution2(num2,num1))




print(10**(len(num1)-1), 10**(len(num2)-1) )

print("solution: 8762")

print(ord("8"))
print(ord("4"))
print(ord("3"))
print(ord("2"))
print(ord("0"))
print(ord("8") - ord("0"))
print(ord("4") - ord("0"))
print(ord("3") - ord("0"))
print(ord("2") - ord("0"))