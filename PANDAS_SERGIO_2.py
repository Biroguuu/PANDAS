#EXPT 8_ PROBLEM 2 _ SERGIO _ 2ECE-A 
import pandas as pd 

cars = pd.read_csv('cars.csv')

cd = pd.DataFrame(cars, columns = ['Model', 'mpg', 'cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb' ])

#A
print(cd.iloc[1:10:2])
#B
print(cd.iloc[:1])
#C
print(cd.loc[[23],['Model','cyl']])
#D
print(cd.iloc[[1, 28, 18],[0,2,10]])