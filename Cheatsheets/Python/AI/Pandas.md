### **Pandas Cheat Sheet:**

**1. Import Pandas:**
```python
import pandas as pd
```
**Explanation:** Import Pandas and alias it as `pd` for convenience.

---

**2. Creating a DataFrame:**
```python
# From a Dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# From a List of Lists
data_list = [['Alice', 25], ['Bob', 30], ['Charlie', 35]]
df_list = pd.DataFrame(data_list, columns=['Name', 'Age'])
```
**Explanation:** Creating a DataFrame from a dictionary or a list of lists.

---

**3. Loading Data:**
```python
# From CSV File
df_csv = pd.read_csv('data.csv')

# From Excel File
df_excel = pd.read_excel('data.xlsx')
```
**Explanation:** Loading data into a DataFrame from CSV or Excel files.

---

**4. DataFrame Information:**
```python
# Display First n Rows
first_rows = df.head(2)

# Display Last n Rows
last_rows = df.tail(2)

# DataFrame Information
info = df.info()
```
**Explanation:** Displaying the first and last rows of a DataFrame and providing information about the DataFrame.

---

**5. Indexing and Selection:**
```python
# Select Column
name_column = df['Name']

# Select Multiple Columns
selected_columns = df[['Name', 'Age']]

# Select Row by Index
row_by_index = df.loc[1]

# Select Rows by Condition
selected_rows = df[df['Age'] > 30]
```
**Explanation:** Indexing and selecting data from a DataFrame.

---

**6. Data Cleaning:**
```python
# Handling Missing Values
df_cleaned = df.dropna()

# Filling Missing Values
df_filled = df.fillna(0)

# Removing Duplicates
df_no_duplicates = df.drop_duplicates()
```
**Explanation:** Cleaning data by handling missing values and removing duplicates.

---

**7. Data Manipulation:**
```python
# Adding a New Column
df['Salary'] = [50000, 60000, 70000]

# Applying a Function
df['Age_squared'] = df['Age'].apply(lambda x: x**2)

# Grouping and Aggregating
grouped_data = df.groupby('Age').agg({'Salary': 'mean'})
```
**Explanation:** Manipulating data by adding columns, applying functions, and grouping.

---

**8. Merging and Concatenating:**
```python
# Concatenating DataFrames
df_concatenated = pd.concat([df1, df2], axis=0)

# Merging DataFrames
df_merged = pd.merge(df1, df2, on='common_column')
```
**Explanation:** Combining DataFrames through concatenation and merging.

---

**9. Time Series Operations:**
```python
# Creating a DateTime Index
df_time = pd.DataFrame(data={'value': [10, 20, 15]}, index=pd.to_datetime(['2022-01-01', '2022-01-02', '2022-01-03']))

# Resampling Time Series Data
df_resampled = df_time.resample('D').mean()
```
**Explanation:** Working with time series data by creating DateTime indices and resampling.

---

**10. Exporting Data:**
```python
# Save DataFrame to CSV
df.to_csv('output.csv', index=False)

# Save DataFrame to Excel
df.to_excel('output.xlsx', index=False)
```
**Explanation:** Exporting DataFrame to CSV or Excel files.

---

**11. Advanced DataFrame Operations:**
```python
# Pivot Table
pivot_table = df.pivot_table(values='Salary', index='Name', columns='Age', aggfunc='mean')

# Apply Function to Rows or Columns
df['Total'] = df.apply(lambda row: row['Age'] + row['Salary'], axis=1)
```
**Explanation:** Performing advanced operations like pivot tables and applying functions to rows or columns.

---

**12. Data Visualization with Pandas:**
```python
# Plotting DataFrame
df.plot(x='Age', y='Salary', kind='scatter')

# Plotting Histogram
df['Age'].plot(kind='hist', bins=10)
```
**Explanation:** Creating simple visualizations using Pandas plotting capabilities.

---

