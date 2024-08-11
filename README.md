# Exploratory Data Analysis (EDA) on Used Cars Dataset

This repository contains a comprehensive exploratory data analysis (EDA) on a used cars dataset. The purpose of this analysis is to gain insights into the dataset, understand the relationships between different features, and identify any patterns or anomalies.

## Dataset Description

The dataset contains various attributes of used cars, including but not limited to:

- **Name**: Name of the car
- **Location**: The location where the car is being sold or is available for purchase
- **Year**: The year the car was purchased
- **Kilometers_Driven**: The distance completed by the car in kilometers
- **Fuel_Type**: The type of fuel used by the car
- **Transmission**: The type of transmission used by the car (Automatic/Manual)
- **Owner_Type**: The type of ownership
- **Mileage**: The mileage offered by the car
- **Engine**: The engine capacity of the car
- **Power**: The maximum power of the car
- **Seats**: The number of seats in the car
- **New_Price**: The price of the car when it was new
- **Price**: The current price of the car

## Analysis Summary

### Data Preprocessing

- Removed unnecessary columns (e.g., `S.No.`).
- Extracted brand and model information from the car names.
- Calculated the age of the car based on the year of purchase.
- Handled missing values in the dataset by filling with median values based on grouping by relevant features.

### Data Transformation

- Applied log transformation to `Kilometers_Driven` and `Price` columns to handle skewness.

### Visualizations

- Histograms and box plots for numerical columns to understand the distribution and detect outliers.
- Bar plots for categorical columns to visualize the frequency distribution of categories.
- Pair plots to visualize relationships between different features.
- Heatmap to show the correlation between numerical features.

### Example Visualizations

1. **Histograms and Box Plots**: Visualized distributions of numerical features like `Kilometers_Driven` and `Price`.
2. **Bar Plots**: Displayed the count of different `Fuel_Type`, `Transmission`, `Owner_Type`, and more.
3. **Pair Plots**: Showed relationships between log-transformed numerical features.
4. **Correlation Heatmap**: Illustrated the correlation between different numerical features.
