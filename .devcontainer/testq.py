# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file 
data = pd.read_excel('/kaggle/input/child-mortality/child-mortality-1990-vs-latest-slope.xlsx')

# Create dataframe with relevant columns
df = data[['Country', 'MortalityRate', 'Population']] 

# Group data by country and calculate averages
country_data = df.groupby('Country').mean()

# Create bar chart comparing infant mortality rates
country_data['MortalityRate'].plot(kind='bar')
plt.title('Mortality Rates By Country')
plt.ylabel('Deaths per 1000 Births')
plt.xlabel('Country')

# Create scatter plot comparing prenatal care and mortality
k = (country_data['Population'], country_data['MortalityRate'])
plt.hist(k)
plt.title('Population vs. Infant Mortality')
plt.xlabel('Population')  
plt.ylabel('Mortality Rate')
plt.savefig('population_vs_mortality.png')

print('Data analysis and visualizations complete.')
plt.show() 