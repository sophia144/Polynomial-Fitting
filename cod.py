#importing required modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#cleaning the dataset
full_df = pd.read_csv('long-term-cod-catch.csv')
full_df.drop(columns=['Code'], inplace=True)
recent_df = full_df[full_df['Year'] > 1920]

#setting up parameters for plotting
x_axis = "Year"
x_axis_label = "Year"
y_axis = "Northern Atlantic cod catch"
y_axis_label = "Cod Catch"

y_coefficient_word = "(millions)"
y_coefficient_figure = 1000000

title = "Polynomial Fits for Northern Atlantic Cod Catches in Eastern Canada"

#writing coordinates to numpy arrays
x_coords = recent_df[x_axis]
y_coords = recent_df[y_axis]/y_coefficient_figure

#plotting the main data
plt.plot(x_coords, y_coords)
plt.xlabel(x_axis)
plt.ylabel(f"{y_axis_label} {y_coefficient_word}")
plt.title(title)

#polynomial fits
for order in range(1, 10):
    #calculations and plotting
    coefficients = np.polyfit(x_coords, y_coords, order)
    poly_function = np.poly1d(coefficients)
    plt.plot(x_coords, poly_function(x_coords), alpha=0.3)
    
    #working out chi squared
    uncertainty = 1
    residuals = y_coords - poly_function(x_coords)
    chi_squared = np.sum((residuals/uncertainty)**2)


plt.show()
