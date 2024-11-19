from pars_data import load
import matplotlib.pyplot as plt
import numpy as np

    
def main():
    

    data = load("./Dataset/data.csv")
    data_meileage,data_price = data["km"],data["price"]
    theta = load("./Dataset/theta.csv")
    theta0=theta["theta0"]
    theta1=theta["theta1"]
    try:
        arg = input("Please Enter a mileage: ")
        try:
            if float(arg) > 0:
                e_price = np.array(theta0)[-1] + np.array(theta1)[-1] * float(arg)
                print(f"the estimated price of the car is {e_price} Euro")
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
