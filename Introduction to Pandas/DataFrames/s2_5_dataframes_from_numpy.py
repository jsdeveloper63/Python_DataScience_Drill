import numpy as np
import pandas as pd

# Create a numpy array
new_array = np.arange(0,50).reshape(10,5)
#print(new_array)

# Convert numpy array into DataFrame
df = pd.DataFrame(data=new_array, columns=['A', 'B', 'C', 'D', 'E'])
print(df)
new_array = np.arange(0,60).reshape(10,6)
#print(new_array)
#print(new_array[1:2])

df = pd.DataFrame(data = new_array, columns = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6'])
#print(df)
