import pandas as pd
import os 
import numpy as np

def load(path: str) -> pd.DataFrame:
    
    try:
        if os.path.exists(path) and path.lower().endswith('.csv'):
            data = pd.read_csv(path)
            print(f"Loading dataset of dimensions: {data.shape}")
            return data
        else:
            raise AssertionError("File not in CSV format")
    except FileNotFoundError:
        print(f"Error: File not found - {path}")
    except PermissionError:
        print(f"Error: Permission denied - {path}")
    except AssertionError as error:
        print(f"AssertionError: {error}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return None


def load_theta(path: str):
   
    try:
    
        if not os.path.exists(path) or not path.lower().endswith('.csv'):
            raise FileNotFoundError(f"File not found or not a CSV: {path}")

        with open(path, 'r') as file:
            lines = file.readlines()

        if len(lines) < 2:
            raise ValueError("Invalid theta file: Missing header or values")

        header = lines[0].strip().split(',')
        if header != ["theta0", "theta1"]:
            raise ValueError("Invalid theta file format: First line must be 'theta0,theta1'")

        theta_values = np.loadtxt(lines[1:], delimiter=',', ndmin=2)

       
        if theta_values.shape[1] != 2:
            raise ValueError("Invalid theta file format: Each row must have two values")

        theta0, theta1 = theta_values[:, 0], theta_values[:, 1]

        return {"theta0": theta0, "theta1": theta1}

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return None
