import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
file_path = 'World_Population_CountryWise_RAW.csv'
data = pd.read_csv(file_path)

# Preprocess the dataset

# Remove the first 3 rows and reset the index
data_cleaned = data.iloc[3:].reset_index(drop=True)

# Set the first row as the header
data_cleaned.columns = data_cleaned.iloc[0]

# Drop the first row now that it has been set as the header
data_cleaned = data_cleaned.drop(0).reset_index(drop=True)


# Convert columns to appropriate data types
data_cleaned.columns = [str(col) for col in data_cleaned.columns]
for col in data_cleaned.columns[4:]:
    data_cleaned[col] = pd.to_numeric(data_cleaned[col], errors='coerce')


# Handle missing values (if any)
data_cleaned.fillna(0, inplace=True)

# Summary statistics calculations
summary_statistics = data_cleaned.describe()

# Mean population by year
mean_population = data_cleaned.mean(numeric_only=True)

# Median population by year
median_population = data_cleaned.median(numeric_only=True)

# Mode population by year (mode can be multiple values, handle accordingly)
mode_population = data_cleaned.mode().iloc[0]

# Standard deviation population by year
std_population = data_cleaned.std(numeric_only=True)

# Visualizations

# Population trends over the years
plt.figure(figsize=(12, 6))

#select all rows (:) and columns from '1960.0' to '2023.0'
# sns.lineplot(data=data_cleaned.loc[:, '1960.0':'2023.0'].mean(), marker='o')
#
# plt.title('Average Population Trends (1960-2023)')
# plt.xlabel('Year')
# plt.ylabel('Average Population')
# plt.xticks(rotation=45)
# plt.grid(True)
# plt.tight_layout()
#
# plt.show()



# Plotting population trends over the years
years = mean_population.index.astype(float)

plt.figure(figsize=(14, 7))
plt.plot(years, mean_population, label='Mean', marker='o')
plt.plot(years, median_population, label='Median', marker='o')
plt.plot(years, mode_population[4:], label='Mode', marker='o')  # Skip first four non-year columns
plt.plot(years, std_population, label='Standard Deviation', marker='o')

plt.title('Population Trends (1960-2023)')
plt.xlabel('Year')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()

#distribution
plt.figure(figsize=(12, 6))
sns.histplot(data_cleaned['2023.0'], kde=True)
plt.title('Population Distribution in 2023')
plt.xlabel('Population')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()

plt.show()
