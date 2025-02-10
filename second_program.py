from pars_data import load
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def normalize_array(arr):
    norm_arr = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
    return norm_arr

def denormalize_coefficients(theta0, theta1, km, price):
    range_km = np.max(km) - np.min(km)
    range_price = np.max(price) - np.min(price)

    theta1_denorm = theta1 * (range_price / range_km)
    theta0_denorm = theta0 * range_price + np.min(price)

    return theta0_denorm, theta1_denorm

def train(m, p, alpha):
    theta0 = 0
    theta1 = 0
    i = 0
    while i < 10000:
        gradient_theta0 = np.mean(theta1 * m + theta0 - p)
        gradient_theta1 = np.mean((theta1 * m + theta0 - p) * m)

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
    data_mileage, data_price = data["km"], data["price"]
 
    km = normalize_array(np.array(data_mileage))
    price = normalize_array(np.array(data_price))

    alpha =0.1
    theta0, theta1 = train(km, price, alpha)
    theta0_real, theta1_real = denormalize_coefficients(theta0, theta1, data_mileage, data_price)
   
    theta_df = pd.DataFrame({"theta0": [theta0_real], "theta1": [theta1_real]})
    theta_df.to_csv("./Dataset/theta.csv", mode="a", header=False, index=False)
    print(theta0_real)

    plt.xlabel('km')
    plt.ylabel('price')
    plt.title("Mileage of Car")
    plt.scatter(data_mileage, data_price, label="Data points")
    plt.plot(data_mileage, theta1_real * data_mileage + theta0_real, color="red", label="Regression line")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
