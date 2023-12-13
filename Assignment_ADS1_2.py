# -*- coding: utf-8 -*-
"""Assigment2.ipynb
### Importing Important Libraries
"""

import pandas as pd # import panda library as pd for data manipulation
import matplotlib.pyplot as plt # import matplotlib as plt for data visualitzation
from matplotlib import style
import numpy as np # import nump as np
import seaborn as sns # seaborn is data visualization library build on matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

"""### Implement a Function Which return Original DataFrame, Transposed DataFrames"""

def transpose_file(filename: str):

    # Read the file into a pandas dataframe
    dataframe = pd.read_csv(filename)

    # Transpose the dataframe
    df_transposed = dataframe.transpose()

    # Populate the header of the transposed dataframe with the header information

    # silice the dataframe to get the year as columns
    df_transposed.columns = df_transposed.iloc[1]

    # As year is now columns so we don't need it as rows
    transposed_year = df_transposed[0:].drop('year')

    # silice the dataframe to get the country as columns
    df_transposed.columns = df_transposed.iloc[0]

    # As country is now columns so we don't need it as rows
    transposed_country = df_transposed[0:].drop('country')

    return dataframe, transposed_country, transposed_year

# Passing filename to Real Worldbank data function
# will return three dataframe:
# org dataframe, transposed country as columns and transposed year as column

org_df, df_by_country, df_by_year = transpose_file('worldbank_dataset.csv')

"""### Original DataFrame"""

# show the first 5 row
org_df.head(5)

"""### show the statistics of Original Data"""

org_df.describe() #describe method show the statistic of dataframe

"""### DataFrame In Which Countries are Columns"""

# show the first 5 row
df_by_country.head(5)

"""### DataFrame In Which Year are Columns"""

# show the first 5 row
df_by_year

org_df.columns

"""### Create DataFrame related to fresh_water
### For All the countries and years
"""

# we want to see countries fresh_water over specfic years
# we need to filter our original data frame to get specific fields

# Filter the data for non-null values
fresh_water = org_df[['country', 'year', 'fresh_water']].dropna()

"""### Get Data to Specific Years from 1990 to 2020"""

import random

# Define the years for which you want to plot data
years_to_plot = [1990, 2000, 2010, 2015]

# Get a list of all named colors in Matplotlib
all_colors = list(mcolors.CSS4_COLORS.keys())

# Select a specific number of random colors from the list
num_colors_to_select = 20  # You can change this number as needed
selected_colors = random.sample(all_colors, num_colors_to_select)

countries = fresh_water.country.unique()
countries

"""### Plot Barplot"""

# Create a figure and set its size
plt.figure(figsize=(15, 10))

# Set width of bars
barWidth = 0.1

for i, year in enumerate(years_to_plot):
    data = fresh_water[fresh_water['year'] == year]
    plt.bar(np.arange(data.shape[0]) + (0.2 * i), data['fresh_water'], color=selected_colors[i], width=barWidth, label=str(year))

# Show legends, labels, and title
plt.legend()
plt.xlabel('Country', fontsize=15)
plt.title("Fresh Water", fontsize=15)

# Add country names to the x-axis ticks
plt.xticks(np.arange(len(countries)) + 0.2, countries, fontsize=10, rotation=45)

# Show the plot
plt.show()

org_df.columns

"""### Get data of forest_area over the years"""

# we want to see countries urban_population over specfic years
# we need to filter our original data frame to get specific fields

# Filter the data for non-null values
urban_population = org_df[['country', 'year', 'urban_population']].dropna()

"""### Filter from specific year from 1990 to 2020"""

import random

# Define the years for which you want to plot data
years_to_plot = [1990, 2000, 2010, 2015, 2020]

# Get a list of all named colors in Matplotlib
all_colors = list(mcolors.CSS4_COLORS.keys())

# Select a specific number of random colors from the list
num_colors_to_select = 10  # You can change this number as needed
selected_colors = random.sample(all_colors, num_colors_to_select)

countries = urban_population.country.unique()

"""### PLOT barplot"""

# Create a figure and set its size
plt.figure(figsize=(15, 10))

# Set width of bars
barWidth = 0.1

for i, year in enumerate(years_to_plot):
    data = urban_population[urban_population['year'] == year]
    plt.bar(np.arange(data.shape[0]) + (0.2 * i), data['urban_population'], color=selected_colors[i], width=barWidth, label=str(year))

# Show legends, labels, and title
plt.legend()
plt.xlabel('Country', fontsize=15)
plt.title("Urban Population", fontsize=15)

# Add country names to the x-axis ticks
plt.xticks(np.arange(len(countries)) + 0.2, countries, fontsize=10, rotation=45)

# Show the plot
plt.show()

org_df.country.unique()

"""### Making a DataFrame related to Albania"""

# making dataframe of Albania data from the original dataframe
alb = org_df[org_df['country'] == 'Albania']

"""### Implement a Function which removes Null values and return clean data"""

def remove_null_values(feature):
    return np.array(feature.dropna())

"""### For the Features Present In Albania DataFrame remove the null values
### Print Each Features Size
"""

org_df.columns

# List of columns to extract
columns_of_interest = ['agricultural_land', 'greenhouse_gas_emissions',
       'rural_population', 'cereal_yield', 'urban_population', 'GDP',
       'fresh_water', 'forest_area', 'renewable_electricity',
       'alternative_energy']

# Dictionary to store feature data after removing null values
feature_data = {}

# Loop through each column to extract and clean the data
for column in columns_of_interest:
    feature_data[column] = remove_null_values(alb[[column]])
    print(f'{column} Length = {len(feature_data[column])}')

# Create data_sources dictionary dynamically
data_sources = {column: feature_data[column] for column in columns_of_interest}

# Determine the number of rows to include
num_rows = 25

# Create the DataFrame using dictionary comprehension
alb_clean_data = pd.DataFrame({
    key: [data_sources[key][x][0] for x in range(num_rows)] for key in data_sources
})

import seaborn as sns
import matplotlib.pyplot as plt

# Create a correlation matrix
correlation_matrix = alb_clean_data.corr()

# Create a heatmap using Seaborn
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='YlGnBu', fmt=".2f")
plt.title('Correlation Heatmap for Albania')
plt.show()

correlation_matrix

org_df.country.unique()

"""### Making a DataFrame related to Belize"""

# making dataframe of Belize data from the original dataframe
bel = org_df[org_df['country'] == 'Belize']

"""### For the Features Present In DataFrame remove the null values
### Print Each Features Size
"""

bel.columns

# List of columns to extract
columns_of_interest = ['agricultural_land', 'greenhouse_gas_emissions',
       'rural_population', 'cereal_yield', 'urban_population', 'GDP',
       'fresh_water', 'forest_area', 'renewable_electricity',
       ]

# Dictionary to store feature data after removing null values
feature_data = {}

# Loop through each column to extract and clean the data
for column in columns_of_interest:
    feature_data[column] = remove_null_values(bel[[column]])
    print(f'{column} Length = {len(feature_data[column])}')

# Create data_sources dictionary dynamically
data_sources = {column: feature_data[column] for column in columns_of_interest}

# Determine the number of rows to include
num_rows = 31

# Create the DataFrame using dictionary comprehension
bel_clean_data = pd.DataFrame({
    key: [data_sources[key][x][0] for x in range(num_rows)] for key in data_sources
})

import seaborn as sns
import matplotlib.pyplot as plt

# Create a correlation matrix
correlation_matrix = bel_clean_data.corr()

# Create a heatmap using Seaborn
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='Blues', fmt=".2f")
plt.title('Correlation Heatmap for Belize')
plt.show()

correlation_matrix

org_df.country.unique()

"""### Making a DataFrame related to Sri Lanka"""

# making dataframe of Sri Lanka data from the original dataframe
sri = org_df[org_df['country'] == 'Sri Lanka']

"""### For the Features Present In DataFrame remove the null values
### Print Each Features Size
"""

sri.columns

# List of columns to extract
columns_of_interest = [ 'agricultural_land', 'greenhouse_gas_emissions',
       'rural_population', 'cereal_yield', 'urban_population', 'GDP',
       'fresh_water', 'forest_area', 'renewable_electricity',
       'alternative_energy']

# Dictionary to store feature data after removing null values
feature_data = {}

# Loop through each column to extract and clean the data
for column in columns_of_interest:
    feature_data[column] = remove_null_values(sri[[column]])
    print(f'{column} Length = {len(feature_data[column])}')

# Create data_sources dictionary dynamically
data_sources = {column: feature_data[column] for column in columns_of_interest}

# Determine the number of rows to include
num_rows = 25

# Create the DataFrame using dictionary comprehension
sri_clean_data = pd.DataFrame({
    key: [data_sources[key][x][0] for x in range(num_rows)] for key in data_sources
})

import seaborn as sns
import matplotlib.pyplot as plt

# Create a correlation matrix
correlation_matrix = sri_clean_data.corr()

# Create a heatmap using Seaborn
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='Greens', fmt=".2f")
plt.title('Correlation Heatmap for Sri Lanka')
plt.show()

correlation_matrix

org_df.columns

"""### Get the Year, Country Data Related to rural_population"""

# we want to see countries rural_population over the years
# we need to filter our original data frame to get specific fields
rural_population = org_df[['country','year','rural_population']]

# drop the null values present in the dataset
rural_population  = rural_population.dropna()

"""### Filter the Data For All the Countries"""

# Define countries of interest
countries = org_df.country.unique()
countries

"""### Line Plot of Rural Population"""

# Set fig size
plt.figure(figsize=(15, 10))

# Loop through countries and plot population_growth over the years
for country in countries:
    country_data = rural_population[rural_population['country'] == country]
    plt.plot(country_data['year'], country_data['rural_population'], label=country)

# Set X-axis label and title
plt.xlabel('Year', fontweight='bold')
plt.title("Rural Population")

# Show legends and plot
plt.legend(bbox_to_anchor=(0.89, 0.7), shadow=True)
plt.show()

"""### Get the Year, Country Data Related to cereal_yield"""

# we want to see countries cereal_yield over the years
# we need to filter our original data frame to get specific fields
cereal_yield = org_df[['country','year','cereal_yield']]

# drop the null values present in the dataset
cereal_yield  = cereal_yield.dropna()

"""### Filter the Data For All the Countries"""

# Define countries of interest
countries = org_df.country.unique()
countries

"""### Line Plot of cereal_yield"""

# Set fig size
plt.figure(figsize=(15, 10))

# Loop through countries and plot cereal_yield over the years
for country in countries:
    country_data = cereal_yield[cereal_yield['country'] == country]
    plt.plot(country_data['year'], country_data['cereal_yield'], label=country)

# Set X-axis label and title
plt.xlabel('Year', fontweight='bold')
plt.title("Cereal Yield")

# Show legends and plot
plt.legend(bbox_to_anchor=(0.89, 0.7), shadow=True)
plt.show()

org_df.columns

# we want to see countries GDP over the years
forest_area = org_df[['country','year','forest_area']]

# drop the null values present in the dataset
forest_area = forest_area.dropna()

### Filter from specific year from 1990 to 2015
# filter data related to 1990
forest_area_1990 = forest_area[forest_area['year'] == 1990]

# filter data related to 2010
forest_area_2010 = forest_area[forest_area['year'] == 2010]

# filter data related to 2020
forest_area_2020 = forest_area[forest_area['year'] == 2020]

forest_area_1990

forest_area_2010

forest_area_2020