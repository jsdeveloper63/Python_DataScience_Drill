import pandas as pd

df = pd.read_csv('../../sample_data/02 Introduction to Pandas/intel.csv')

# Print the Open column
open =df['Open']
#print(df['Open'])
# Create a new variable and print its type to confirm it's a numpy array
new_open = open.values
#print(type(new_open))

# Print the values contained in new_open
#print(new_open)
#print(df.info())

high = df['High']
new_high = high.values
#print(new_high)
#print(type(new_high))
#print(df['Date'])
date = df['Date']
new_date = date.values
#print(type(new_date))
print(df(df(new_date)))
