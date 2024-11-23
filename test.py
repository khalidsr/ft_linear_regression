import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def load(filepath):
    return pd.read_csv(filepath)

def main():
    data = load("./Dataset/data.csv")
    data_meileage, data_price = data["km"], data["price"]
 
    x = np.array(data_meileage)
    y = np.array(data_price)
    
    # Fit the linear regression model
    coefficients = np.polyfit(x, y, 1, cov=True)
    print("Linear Fit Coefficients:", coefficients)
    
    slope = coefficients[0][0]
    intercept = coefficients[0][1]
    print(slope, intercept)
    
    # Generate line points
    line_x = np.linspace(min(x), max(x), 100)
    line_y = slope * line_x + intercept
    # computed_slope, computed_intercept = coefficients
    # absolute_error_slope = abs(computed_slope - true_slope)
    # relative_error_slope = absolute_error_slope / true_slope

    # print(f"Absolute Error in Slope: {absolute_error_slope}")
    # print(f"Relative Error in Slope: {relative_error_slope}")
    plt.xlabel('km')
    plt.ylabel('price')
    plt.title("Mileage of Car")
    plt.scatter(x, y, label="Data points")
    plt.plot(line_x, line_y, color="red", label="Regression line")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

