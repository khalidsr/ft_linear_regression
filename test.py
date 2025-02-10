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
    
    coefficients = np.polyfit(x, y, 1, cov=True)
    print("Linear Fit Coefficients:", coefficients)
    
    slope = coefficients[0][0]
    intercept = coefficients[0][1]
    print(slope, intercept)
    

    line_x = np.linspace(min(x), max(x), 100)
    line_y = slope * line_x + intercept

    plt.xlabel('km')
    plt.ylabel('price')
    plt.title("Mileage of Car")
    plt.scatter(x, y, label="Data points")
    plt.plot(line_x, line_y, color="red", label="Regression line")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

