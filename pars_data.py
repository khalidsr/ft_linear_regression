import pandas as pd

def load(path: str) ->pd:
    """
    This function takes a path as argument print the dimensions of the data set
    and returns it. it return None if the path is bad or an exception wa thrown.
    """
    try:
        if path.lower().endswith('.csv'):
            data = pd.read_csv(path)
            print(f"Loading dataset of dimensions: {data.shape}")
            return data
        else:
            raise AssertionError("file not csv format")
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
    except AssertionError as error:
        print(AssertionError.__name__,error)

    return None
