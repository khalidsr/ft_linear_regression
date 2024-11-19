from pars_data import load
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
# def train(mileage)
    
def main():
    

    data = load("./Dataset/data.csv")
    data_meileage,data_price = data["km"],data["price"]
    # theta = load("./Dataset/theta.csv")
    theta0=0
    # theta1=1
    # theta_df = pd.DataFrame({"theta0": [theta0], "theta1": [theta1]})
    # plt.scatter(data['km'], data['price'])

    alpha = random.random()
    y = theta0 + theta1*np.arr(data['km'])
    
    
  
    # plt.xlabel('km')
    # plt.ylabel('price')
    # plt.title("mileage of car")
    # plt.show()
    # theta_df.to_csv("./Dataset/theta.csv", mode="a", header=False, index=False)
    
if __name__=="__main__":
    main()
