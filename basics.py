import os
import pandas as pd
import matplotlib.pyplot as plt

''' If the index of a pandas DataFrame consists of dates, 
then pandas will automatically format the x-axis in a human-readable way'''

home_path = os.path.dirname(__file__)

# DataFrame
train_path = home_path+"TrainingSet.csv"

trainingData = pd.read_csv(train_path)

# Display the first five lines of the DataFrame
print(trainingData.head(n=5))

# Print the data type of each column in trainingData
print(trainingData.dtypes)

# Convert the date column to a datestamp type
# trainingData['date'] = pd.to_datetime(trainingData['date'])
# print(trainingData.dtypes)

# Set the date column as the index of your DataFrame discoveries
trainingData = trainingData.set_index('PRICE')

# Slicing time series data and assign it to a new dataframe, then plot subset ax = df_subset.plot()
# df_subset = trainingData['1960':'1970'] | trainingData['1960-02':'1970-05'] | trainingData['1960-02-01':'1970-05-31']

''' The plot function returns a matplotlib AxesSubplot object, and it is common practise to assign this returned object to a 
    variable called ax. Doing so also allows you to include additional notations and specifications to your plot such as axis labels. '''
# Plot the time series in your DataFrame
ax = trainingData.plot(color='blue', figsize=(8,5), fontsize=12, linewidth=3, linestyle='--')

''' Using markers '''
# Vertical line:
ax.axvline(x=500000, color='red', linestyle='--') # eg. x='1966-05-10'
# Horizontal line:
ax.axhline(y=100000, color='green', linestyle='--')

''' Highlighting regions of interest '''
ax.axvspan(500000, 10000, color='red', alpha=0.5) # alpha: transparency
ax.axhspan(80000, 160000, color='green', alpha=0.2)

ax.set_title('Plotting PRICE', fontsize=16)

# Specify the x-axis label in your plot
ax.set_xlabel('Other variables', fontsize=13)

# Specify the y-axis label in your plot
ax.set_ylabel('Price', fontsize=13)

print(plt.style.available)
plt.style.use('fivethirtyeight')

# Show plot
plt.show()

ax2 = trainingData.plot()
plt.style.use('ggplot')
# Set the title
ax2.set_title('ggplot Style')
plt.show()