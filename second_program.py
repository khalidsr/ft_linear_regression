from pars_data import load
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def normalize_array(arr):
    norm_arr = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
    return norm_arr

def train(m, p, alpha):
    theta0 = 0
    theta1 = 0
    i = 0
    while i < 1000:

        gradient_theta0 = np.mean(theta1 * m + theta0 - p)
        gradient_theta1 = np.mean((theta1 * m + theta0 - p) * m)
        print(theta0,"---------------|",i,"|-------------",theta1)
        plt.plot(m, theta1 * m + theta0, color="red",)


        temp_theta0 = theta0 - alpha * gradient_theta0
        temp_theta1 = theta1 - alpha * gradient_theta1

        if temp_theta0 == theta0 and temp_theta1 == theta1:
            print("Convergence found")
            break

        theta0 = temp_theta0
        theta1 = temp_theta1
        i += 1

    return theta0, theta1

def main():

    data = load("./Dataset/data.csv")
    data_meileage, data_price = data["km"], data["price"]
 
    km = normalize_array(np.array(data_meileage))
    price = normalize_array(np.array(data_price))

    alpha = 0.9
    theta0, theta1 = train(km, price, alpha)


    theta_df = pd.DataFrame({"theta0": [theta0], "theta1": [theta1]})
    theta_df.to_csv("./Dataset/theta.csv", mode="a", header=False, index=False)

    plt.xlabel('km')
    plt.ylabel('price')
    plt.title("Mileage of Car")
    plt.scatter(km, price, label="Data points")
    plt.plot(km, theta1 * km + theta0, color="red", label="Regression line")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
