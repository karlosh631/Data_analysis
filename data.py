import pandas as pd
import matplotlib.pyplot as plt


file_path = 'C:/Users/sharm/Downloads/2025-01-29 Modern Bhatti june-month_ vegetables prices(Sheet1).csv'
df = pd.read_csv(file_path)


# here the 1st column is 'Vegetables', and the rest are dates
new_column_names = ['Vegetables']  # Start with the 'Vegetables' as the first column name

# Extracting date part from column names and adding them to the list.
for col in df.columns[1:]:  # Skip the first column as it is assigned as 'vegetables' already so
    new_column_names.append(col.split(":")[1])  # Extract date part as name 'vegetables':dates.

df.columns = new_column_names  # Rename columns

#  Remove the first row (it contains extra labels)
df = df.iloc[1:].reset_index(drop=True)  # Remove first row and reset index

#  To Convert all prices to numeric values and for error='coerce'
df.iloc[:, 1:] = df.iloc[:,1:].apply(pd.to_numeric, errors='coerce')

#  Set 'Vegetables' as the index
df.set_index('Vegetables', inplace=True)

#  Transpose the data to switch rows and columns
df_transposed = df.T  # Now dates are rows, and vegetables are columns

#  Calculate daily price change
price_change_diff = df_transposed.diff()  # Difference between consecutive days

#  Plot price trends
plt.figure(figsize=(15, 9))  # Set figure size

for vegetable in df.index:  # Loop through each vegetable
    plt.plot(df_transposed.index, df_transposed[vegetable], marker='o', linestyle='-', label=vegetable)

#  Customize the plot

plt.xlabel("Date")  # Label for x-axis
plt.ylabel("Price per kg (Rs)")  # Label for y-axis
plt.title("Vegetable Price")  # Title of the graph
plt.xticks(rotation=45)  # Rotate date labels for better visibility
plt.legend(title='Veg_Names',loc='upper left', bbox_to_anchor=(.99212, 1.12))  # Show legend outside the graph
plt.grid(True)  # Add grid for better readability


plt.show()


print("Price ")
print(price_change_diff)