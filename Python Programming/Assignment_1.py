# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZeTmLeedF7WGu4bDwH0ZXWSad1V9scKx

Assignment 1

Question 1.1
"""

import numpy as np
n1 = np.zeros(10)
n1

n2 = np.ones(10)
n2

n1=np.full((1,10),5)
n1

"""Question 1.2 create an array of all the even
integers from 10 to 50
"""

import numpy as np
print("array of all the even integers from 10 to 50 : ",end="")
arr = np.arange(10,50,2)
arr

"""Question 1.3 Generate number between 0 and 1"""

import numpy as np
print("Random number between 0 and 1 : ")
arr = np.random.rand()
arr

"""Question 1.4 Save and load the matrix"""

import numpy as np
arr = np.random.randint(10,size=(3,3))
np.savetxt('123.txt', arr)
np.loadtxt('123.txt')
arr



"""Question 2.3 Pandas program to create the today's date

"""

from datetime import datetime

print("Today's Date : ",end="")
print(datetime.now().date())

import pandas as pd
from datetime import date
now = pd.to_datetime(str(date.today()), format='%Y-%m-%d')
print("Today's date:")
print(now)

"""Question no. 2(1)"""

from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

import pandas as pd

from PIL import Image
import numpy as np
  
img = Image.open('matrix.png')

matrix = np.asarray(img)

print(matrix.shape)

df = pd.DataFrame(matrix)
df.to_csv("matrix1.csv")

"""Question no. 3 Age calculator"""

from datetime import date
 
def Age_calculator(birthDate):
    days_in_year = 365.2425   
    age = int((date.today() - birthDate).days / days_in_year)
    return age
         
# Driver code
print(Age_calculator(date(2000,6,12)), "years")

