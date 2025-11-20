#importing required modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#cleaning the dataset
full_df = pd.read_csv('long-term-cod-catch.csv')
full_df.drop(columns=['Code'], inplace=True)
start_100_period = 1920
end_100_period = 2020
df_100 = full_df[full_df['Year'] > start_100_period]
df_90 = df_100[full_df['Year'] < end_100_period - 10]

#setting up parameters for plotting
x_axis = "Year"
x_axis_label = "Year"
y_axis = "Northern Atlantic cod catch"
y_axis_label = "Cod Catch"

y_coefficient_word = "(millions)"
y_coefficient_figure = 1000000

title = "Polynomial Fits for Northern Atlantic Cod Catches in Eastern Canada"

#writing coordinates to numpy arrays
x_coords_100 = df_100[x_axis]
y_coords_100 = df_100[y_axis]/y_coefficient_figure

x_coords_90 = df_90[x_axis]
y_coords_90 = df_90[y_axis]/y_coefficient_figure

# ~~~~~~~~~~~~~~~~~~~~~~ GRAPH 1 ~~~~~~~~~~~~~~~~~~~~~~

#plotting the main data
plt.grid(alpha=0.5)
plt.scatter(x_coords_100, y_coords_100, s=12)
plt.xlabel(x_axis)
plt.ylabel(f"{y_axis_label} {y_coefficient_word}")
plt.ylim(-0.2, 1)
plt.xlim(1920, 2020)
plt.title(title, pad=20)

#plotting the ten year mark
plt.axvline(x = end_100_period - 10, color = 'midnightblue', linestyle = 'dotted')

#polynomial fits

order_vals = []
chi_squared_vals = []

for order in range(1, 11):

    #calculations and plotting
    coefficients = np.polyfit(x_coords_90, y_coords_90, order)
    poly_function = np.poly1d(coefficients)

    #chi squared calculation
    residuals = poly_function(x_coords_90) - y_coords_90
    sum_squared_residuals = 0
    for residual in residuals:
        sum_squared_residuals += residual ** 2
    order_vals.append(order)
    chi_squared_vals.append(sum_squared_residuals/len(x_coords_90))

    plt.plot(x_coords_100, poly_function(x_coords_100), color='orange', alpha=0.3, lw=1.8)

plt.show()

# ~~~~~~~~~~~~~~~~~~~~~~ GRAPH 2 ~~~~~~~~~~~~~~~~~~~~~~

#plotting chi squared fits for each polynomial

plt.grid(alpha=0.5)
plt.plot(order_vals, chi_squared_vals)
plt.xlabel('Polynomial Coefficients')
plt.ylabel('Chi-Squared')
plt.title('Number of Polynomial Coefficients vs. Quality of Fit', pad=20)

plt.show()

# ~~~~~~~~~~~~~~~~~~~~~~ GRAPH 3 ~~~~~~~~~~~~~~~~~~~~~~

#plotting BIC for each polynomial
