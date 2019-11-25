import pandas as pd 

cars = pd.read_csv('cars.csv')

cd = pd.DataFrame(cars, columns = ['Model', 'mpg', 'cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb' ])

first = cars.head(n=5)
last = cars.tail(n=5)
print(first)
print(last)

