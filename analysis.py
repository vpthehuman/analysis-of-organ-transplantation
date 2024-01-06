import pandas as pd

# Load the data from the 'Overview - National' sheet
file_path = 'C:\\Users\\green\\Documents\\Downloads\\Organ_Donation_and_Transplantation_Data.xlsx'
overview_national = pd.read_excel(file_path, sheet_name='Overview - National')
# Data cleaning: Handle missing values if any, and check data types
overview_national.dropna(inplace=True)  # Example of handling missing values
overview_national['Year'] = overview_national['Year'].astype(int)  # Ensure 'Year' is of integer type
import matplotlib.pyplot as plt
import seaborn as sns

# Setting the aesthetic style of the plots
sns.set_style("whitegrid")

# Plotting trends in the number of deceased and living organ donors
plt.figure(figsize=(12, 6))
sns.lineplot(data=overview_national, x='Year', y='Number of deceased organ donors recovered', hue='Organ', marker='o')
plt.title('Trend in Number of Deceased Organ Donors Recovered by Organ Type')
plt.ylabel('Number of Donors')
plt.show()

plt.figure(figsize=(12, 6))
sns.lineplot(data=overview_national, x='Year', y='Number of living organ donors recovered', hue='Organ', marker='o')
plt.title('Trend in Number of Living Organ Donors Recovered by Organ Type')
plt.ylabel('Number of Donors')
plt.show()

# Plotting trends in the number of organ transplant recipients
plt.figure(figsize=(12, 6))
sns.lineplot(data=overview_national, x='Year', y='Number of deceased donor organ transplant recipients', hue='Organ', marker='o')
plt.title('Trend in Number of Deceased Donor Organ Transplant Recipients by Organ Type')
plt.ylabel('Number of Recipients')
plt.show()

plt.figure(figsize=(12, 6))
sns.lineplot(data=overview_national, x='Year', y='Number of living donor organ transplant recipients', hue='Organ', marker='o')
plt.title('Trend in Number of Living Donor Organ Transplant Recipients by Organ Type')
plt.ylabel('Number of Recipients')
plt.show()
# Create a new DataFrame for donor type comparison
donor_type_comparison = overview_national.groupby(['Year', 'Organ']).agg({
    'Number of deceased organ donors recovered': 'sum',
    'Number of living organ donors recovered': 'sum'
}).reset_index()

# Melt the DataFrame for easier plotting
donor_type_comparison_melted = donor_type_comparison.melt(id_vars=['Year', 'Organ'], 
                                                          var_name='Donor Type', 
                                                          value_name='Number of Donors')

# Plotting comparison of living vs deceased donors for each organ
plt.figure(figsize=(15, 8))
sns.barplot(data=donor_type_comparison_melted, x='Organ', y='Number of Donors', hue='Donor Type')
plt.title('Comparison of Living vs Deceased Donors for Each Organ Type')
plt.xlabel('Organ Type')
plt.ylabel('Number of Donors')
plt.show()
# Calculating the total number of transplants (both deceased and living donor transplants)
overview_national['Total Transplants'] = overview_national['Number of deceased donor organ transplant recipients'] + overview_national['Number of living donor organ transplant recipients']

# Grouping the data by year and organ to calculate the sum of candidates added and transplants done
demand_supply_analysis = overview_national.groupby(['Year', 'Organ']).agg({
    'Number of candidates added': 'sum',
    'Total Transplants': 'sum'
}).reset_index()

# Calculating the gap between demand and supply
demand_supply_analysis['Gap'] = demand_supply_analysis['Number of candidates added'] - demand_supply_analysis['Total Transplants']

# Melt the DataFrame for easier plotting
demand_supply_analysis_melted = demand_supply_analysis.melt(id_vars=['Year', 'Organ'], 
                                                             var_name='Type', 
                                                             value_name='Count')

# Plotting the gap between demand and supply
plt.figure(figsize=(15, 8))
sns.barplot(data=demand_supply_analysis_melted, x='Organ', y='Count', hue='Type')
plt.title('Demand vs Supply Analysis for Each Organ Type')
plt.xlabel('Organ Type')
plt.ylabel('Count')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the 'Overview - National' sheet
file_path = 'C:\\Users\\green\\Documents\\Downloads\\Organ_Donation_and_Transplantation_Data.xlsx'
overview_national = pd.read_excel(file_path, sheet_name='Overview - National')

# Data cleaning: Handle missing values if any, and check data types
overview_national.dropna(inplace=True)  # Example of handling missing values
overview_national['Year'] = overview_national['Year'].astype(int)  # Ensure 'Year' is of integer type

# Convert categorical data (Organ) to numerical data for correlation analysis
overview_national['Organ'] = pd.Categorical(overview_national['Organ'])
overview_national['Organ_Code'] = overview_national['Organ'].cat.codes

# Selecting numerical columns for correlation analysis
numerical_columns = ['Organ_Code', 'Number of deceased organ donors recovered', 
                     'Number of living organ donors recovered', 'Number of candidates added', 
                     'Number of registrations added', 'Number of deceased donor organ transplant recipients', 
                     'Number of living donor organ transplant recipients']

# Calculating the correlation matrix
correlation_matrix = overview_national[numerical_columns].corr()

# Setting the aesthetic style of the plots
sns.set_style("whitegrid")

# Plotting the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap of Organ Transplantation Factors')
plt.show()
