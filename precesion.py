from pars_data import load
import numpy as np

    
def main():
    

    data = load("./Dataset/data.csv")
    data_mileage, data_price = data["km"],data["price"]
    theta = load("./Dataset/theta.csv")
    theta0=theta["theta0"]
    theta1=theta["theta1"]
   
     
    e_price = np.array(theta0)[-1] + np.array(theta1)[-1] * data_mileage
    
    mae = np.mean(np.abs(e_price - data_price))

    accurancy = 100 *(1- mae/(np.max(data_price)-np.min(data_price)))

    print(f"Precision of the algorithm: {accurancy:.2f}%")
  
    
if __name__=="__main__":
    main()
