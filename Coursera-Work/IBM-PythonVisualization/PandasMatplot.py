# Pandas 

import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library
import matplotlib as mpl
import matplotlib.pyplot as plt

df_can = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

print ('Data read into a pandas dataframe!')
print(df_can.head()) # Display top 10 rows
print(df_can.tail()) # Display last 10 rows
print(df_can.info()) # Display column memory and type
print(df_can.columns.values)# Display column Names
print(type(df_can.index))
print(type(df_can.columns))

print(df_can.shape)  #gives two parameters length and width

# Dropping columns
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
print(df_can.head(2))

# Rename columns
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
print(df_can.columns)

# Adding new column with a sum of defined columns
df_can['Total'] = df_can.sum(axis=1)

print(df_can.isnull().sum()) # check to see how many null datasets exist

# Quick Summary of each column in our dataframe using describe()
print(df_can.describe())
# gives count, mean, std, min, 25%, 50%, 75%, max of each column

# filter on column Name
print(df_can.Country)
print(df_can[['Country', 1980,1981,1982,1983,1984,1985]])

######### Select Row ###  Setting Country as an index
df_can.set_index('Country', inplace=True)
print(df_can.head(3))

# Remove Index
df_can.index.name = None
print(df_can.head(3))

# Example: Let's view the number of immigrants from Japan (row 87) for the following scenarios: 1. The full row data (all columns) 2. For year 2013 3. For years 1980 to 1985
print(df_can.loc['Japan'])
# alternate methods
print(df_can.iloc[87])
print(df_can[df_can.index == 'Japan'].T.squeeze())

# 2. for year 2013
print(df_can.loc['Japan', 2013])
# alternate method
print(df_can.iloc[87, 36]) # year 2013 is the last column, with a positional index of 36

# 3. for years 1980 to 1985
print(df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]])
print(df_can.iloc[87, [3, 4, 5, 6, 7, 8]])

# Convert Headers into strings
df_can.columns = list(map(str, df_can.columns))
# [print (type(x)) for x in df_can.columns.values] #<-- uncomment to check type of column headers

#Since we converted the years to string, let's declare a variable that will allow us to easily call upon the full range of years:
years = list(map(str, range(1980, 2014)))
print(years)

############### Filtering based on Criteria
# 1. create the condition boolean series
condition = df_can['Continent'] == 'Asia'
print(condition)

# 2. pass this condition into the dataFrame # appending Step 1 to a new column
df_can[condition]
print(df_can[condition])
df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')]
## Review DF
print('data dimensions:', df_can.shape)
print(df_can.columns)
df_can.head(2)

###################################  MatPlotlib ##################################
print ('Matplotlib version: ', mpl.__version__) # >= 2.0.0
print(plt.style.available)
mpl.style.use(['ggplot']) # optional: for ggplot-like style
haiti = df_can.loc['Haiti', years] # passing in years 1980 - 2013 to exclude the 'total' column
haiti.head()
haiti.plot()

########  Output of the haiti plot
haiti.index = haiti.index.map(int) # let's change the index values of Haiti to type integer for plotting
haiti.plot(kind='line')
plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.show() # need this line to show the updates made to the figure
###### End haiti plot 

#########################  Line Chart 
haiti.plot(kind='line')
plt.title('Immigration from Haiti')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
# annotate the 2010 Earthquake. 
# syntax: plt.text(x, y, label)
plt.text(2000, 6000, '2010 Earthquake') # see note below
plt.show() 
#########################  End Line Chart

