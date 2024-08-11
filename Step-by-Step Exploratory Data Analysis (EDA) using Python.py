import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date
import warnings

warnings.filterwarnings('ignore')

# Load data
data = pd.read_csv("used_cars_data.csv")

# Drop unnecessary columns
data = data.drop(['S.No.'], axis=1)

# Calculate car age
data['Car_Age'] = date.today().year - data['Year']

# Split the Name column into Brand and Model
data['Brand'] = data['Name'].str.split().str.get(0)
data['Model'] = data['Name'].str.split().str.get(1) + ' ' + data['Name'].str.split().str.get(2).fillna('')

# Define categorical and numerical columns
cat_cols = data.select_dtypes(include=['object']).columns
num_cols = data.select_dtypes(include=np.number).columns.tolist()

print("Categorical Variables:")
print(cat_cols)
print("Numerical Variables:")
print(num_cols)

# Visualize numerical columns
for col in num_cols:
    print(f"{col} - Skew: {round(data[col].skew(), 2)}")
    plt.figure(figsize=(15, 4))
    plt.subplot(1, 2, 1)
    data[col].hist(grid=False)
    plt.ylabel('Count')
    plt.subplot(1, 2, 2)
    sns.boxplot(x=data[col])
    plt.show()

# Bar plots for categorical variables
fig, axes = plt.subplots(3, 2, figsize=(18, 18))
fig.suptitle('Bar plot for all categorical variables in the dataset')
sns.countplot(ax=axes[0, 0], x='Fuel_Type', data=data, color='blue', order=data['Fuel_Type'].value_counts().index)
sns.countplot(ax=axes[0, 1], x='Transmission', data=data, color='blue', order=data['Transmission'].value_counts().index)
sns.countplot(ax=axes[1, 0], x='Owner_Type', data=data, color='blue', order=data['Owner_Type'].value_counts().index)
sns.countplot(ax=axes[1, 1], x='Location', data=data, color='blue', order=data['Location'].value_counts().index)
sns.countplot(ax=axes[2, 0], x='Brand', data=data, color='blue', order=data['Brand'].value_counts().index[:20])
sns.countplot(ax=axes[2, 1], x='Model', data=data, color='blue', order=data['Model'].value_counts().index[:20])
axes[1][1].tick_params(labelrotation=45)
axes[2][0].tick_params(labelrotation=90)
axes[2][1].tick_params(labelrotation=90)

# Log transformation function
def log_transform(data, cols):
    for colname in cols:
        data[colname + '_log'] = np.log1p(data[colname])  # Use np.log1p to handle zero values
    data.info()

log_transform(data, ['Kilometers_Driven', 'Price'])

# Log transformation of the feature 'Kilometers_Driven'
plt.figure(figsize=(10, 6))
ax = sns.histplot(data["Kilometers_Driven_log"], kde=True)
ax.set_xlabel("Kilometers_Driven_log")
plt.show()

# Creating pairplot excluding original 'Kilometers_Driven' and 'Price' columns
plt.figure(figsize=(13, 17))
sns.pairplot(data=data.drop(['Kilometers_Driven', 'Price'], axis=1))
plt.show()

# Plotting bar plots for various comparisons
fig, axarr = plt.subplots(4, 2, figsize=(12, 18))
data.groupby('Location')['Price_log'].mean().sort_values(ascending=False).plot.bar(ax=axarr[0][0], fontsize=12)
axarr[0][0].set_title("Location Vs Price", fontsize=18)
data.groupby('Transmission')['Price_log'].mean().sort_values(ascending=False).plot.bar(ax=axarr[0][1], fontsize=12)
axarr[0][1].set_title("Transmission Vs Price", fontsize=18)
data.groupby('Fuel_Type')['Price_log'].mean().sort_values(ascending=False).plot.bar(ax=axarr[1][0], fontsize=12)
axarr[1][0].set_title("Fuel_Type Vs Price", fontsize=18)
data.groupby('Owner_Type')['Price_log'].mean().sort_values(ascending=False).plot.bar(ax=axarr[1][1], fontsize=12)
axarr[1][1].set_title("Owner_Type Vs Price", fontsize=18)
data.groupby('Brand')['Price_log'].mean().sort_values(ascending=False).head(10).plot.bar(ax=axarr[2][0], fontsize=12)
axarr[2][0].set_title("Brand Vs Price", fontsize=18)
data.groupby('Model')['Price_log'].mean().sort_values(ascending=False).head(10).plot.bar(ax=axarr[2][1], fontsize=12)
axarr[2][1].set_title("Model Vs Price", fontsize=18)
data.groupby('Seats')['Price_log'].mean().sort_values(ascending=False).plot.bar(ax=axarr[3][0], fontsize=12)
axarr[3][0].set_title("Seats Vs Price", fontsize=18)
data.groupby('Car_Age')['Price_log'].mean().sort_values(ascending=False).plot.bar(ax=axarr[3][1], fontsize=12)
axarr[3][1].set_title("Car_Age Vs Price", fontsize=18)
plt.subplots_adjust(hspace=1.0)
plt.subplots_adjust(wspace=.5)
sns.despine()

# Correlation heatmap for numeric columns
plt.figure(figsize=(12, 7))
numeric_data = data.select_dtypes(include=[np.number])
sns.heatmap(numeric_data.corr(), annot=True, vmin=-1, vmax=1, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Handling missing values
data.loc[data["Mileage"] == 0.0, 'Mileage'] = np.nan

# Extract numeric part of 'Engine' and 'Power' columns
data['Engine'] = data['Engine'].str.extract('(\d+)').astype(float)
data['Power'] = data['Power'].str.extract('(\d+)').astype(float)

# Impute missing values using group median
data['Seats'] = data.groupby(['Model', 'Brand'])['Seats'].transform(lambda x: x.fillna(x.median()))
data['Engine'] = data.groupby(['Brand', 'Model'])['Engine'].transform(lambda x: x.fillna(x.median()))
data['Power'] = data.groupby(['Brand', 'Model'])['Power'].transform(lambda x: x.fillna(x.median()))

# Checking missing values after handling
print(data.Mileage.isnull().sum())
print(data.Seats.isnull().sum())
