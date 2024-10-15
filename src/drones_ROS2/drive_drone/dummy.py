import pandas as pd

# Define your arrays
array1 = [1, 2, 3]
array2 = [4, 5, 6]
array3 = [7, 8, 9]

# Create a DataFrame from the arrays
df = pd.DataFrame({
    'Array1': array1,
    'Array2': array2,
    'Array3': array3
})

# Write the DataFrame to a CSV file
df.to_csv('arrays.csv', index=False)
