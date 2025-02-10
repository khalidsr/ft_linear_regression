
from pars_data import load
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

def main():
    
    data = load("./Dataset/data.csv")
    if data is None:
        print("Exiting program due to data loading failure.")
        sys.exit(1)
    data_mileage, data_price = data["km"], data["price"]

    theta = load("./Dataset/theta.csv")
    if theta is None:
        print("Exiting program due to theta loading failure.")
        sys.exit(1)
    theta0_real, theta1_real = theta["theta0"].to_numpy()[-1], theta["theta1"].to_numpy()[-1]
    plt.xlabel('km')
    plt.ylabel('price')
    plt.title("Mileage of Car")
    plt.scatter(data_mileage, data_price, label="Data points")
    plt.plot(data_mileage, theta1_real * data_mileage + theta0_real, color="red", label="Regression line")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
