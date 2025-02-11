import sys
from pars_data import load, load_theta
import matplotlib.pyplot as plt
import numpy as np


def main():
    data = load("./Dataset/data.csv")
    
    if data is None:
        print("Exiting program due to data loading failure.")
        sys.exit(1)


    theta = load_theta("./Dataset/theta.csv")

    if theta is None:
        print("Exiting program due to theta loading failure.")
        sys.exit(1)
    theta0, theta1 = theta["theta0"], theta["theta1"]


    try:
        arg = input("Please Enter a mileage: ")
        try:
            if float(arg) >= 0:
                e_price = np.array(theta0)[-1] + np.array(theta1)[-1] * float(arg)
                print(f"The estimated price of the car is {e_price} Euro")
            else:
                raise AssertionError("Enter a valid mileage")
        except ValueError as error:
            print(ValueError.__name__, error)
    except AssertionError as error:
        print(AssertionError.__name__, error)


    # plt.scatter(data['km'], data['price'])
    # theta0 = 0
    # theta1 = 0
    # y=theta0 + theta1*np.arr
    # plt.xlabel('km')
    # plt.ylabel('price')
    # plt.title("mileage of car")
    # plt.show()
    
if __name__=="__main__":
    main()
