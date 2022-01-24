import time
import os
import pandas as pd

# MY_PATH ='/Users/adiaz3/Desktop/python stuff/mega course- 10 apps/processing user input/resources/vegetables.txt'
# while True:
#     if os.path.exists(MY_PATH):
#         with open(MY_PATH) as rfile:
#             print(rfile.read())
#     else:
#         print("file doens't exist")
#     time.sleep(10)

MY_PATH = '/Users/adiaz3/Desktop/python stuff/mega course- 10 apps/modules/data/temps_today.csv'
while True:
    if os.path.exists(MY_PATH):
        data = pd.read_csv(MY_PATH)
        print(data.mean()["st1"])
    else:
        print("file doens't exist")
    time.sleep(10)


