from pars_data import load, load_theta
import numpy as np
import sys

def main():
    

    data = load("./Dataset/data.csv")
    if data is None:
        print("Exiting program due to data loading failure.")
        sys.exit(1)

    data_mileage, data_price = data["km"],data["price"]
    theta = load_theta("./Dataset/theta.csv")
    if theta is None:
        print("Exiting program due to theta loading failure.")
        sys.exit(1)
    theta0=theta["theta0"]
    theta1=theta["theta1"]

    e_price = np.array(theta0)[-1] + np.array(theta1)[-1] * data_mileage
    
    mae = np.mean(np.abs(e_price - data_price))

    accurancy = 100 *(1- mae/(np.max(data_price)-np.min(data_price)))

    print(f"Precision of the algorithm: {accurancy:.2f}%")
  
    
if __name__=="__main__":
    main()
