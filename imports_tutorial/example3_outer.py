# import utils.length
# res = utils.length.get_length("Hello")
# print("the length of the string is:", res)



#adding medium_imports_tutorial/utils to sys path

#METHOD 1
# import os
# import sys

# fpath = os.path.join(os.path.dirname(__file__), 'utils')
# sys.path.append(fpath)
# print(sys.path)

# import length
# import upper
# import lower
# txt = "hello!!"
# res_len = length.get_length(txt)
# print("the length of the string is:", res_len)

# res_up = upper.to_upper(txt)
# print("uppercase txt:", res_up)

# res_low = lower.to_lower(txt)
# print("lowercase txt:", res_low)


#METHOD 2
# use in terminal:
# echo PYTHONPATH (ensure we aren't overwriting it)
#export PYTHONPATH=$PYTHONPATH:$(pwd)/utils

# import length
# txt = "Hellodawggy"
# res_len = length.get_length(txt)
# print("The length of the string is:", res_len)


#time to fix it to where utils is a package with our
#__init__ file
import utils

txt = "Kaio-ken!! Kahh meee Haa mee HAAAA!!"
res_low = utils.to_lower(txt)
print("utils package, lowercase:", res_low)

res_up = utils.to_upper(txt)
print("utils package, uppercase:", res_up)

res_len = utils.get_length(txt)
print("this is the length with utils package:",
res_len)