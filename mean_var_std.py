import numpy as np

def calculate(list):
    # List should contain 9 numbers
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    for n in list:
        if not isinstance(n, int):
            raise ValueError("List must contain nine numbers.")
    x = np.array(list).reshape(3,3)

    calculations = {}

    calculations['mean'] = [nparray_to_list(x.mean(axis=0)), nparray_to_list(x.mean(axis=1)), float(x.mean())]
    calculations['variance'] = [nparray_to_list(x.var(axis=0)), nparray_to_list(x.var(axis=1)), float(x.var())]
    calculations['standard deviation'] = [nparray_to_list(x.std(axis=0)), nparray_to_list(x.std(axis=1)), float(x.std())]
    calculations['max'] = [nparray_to_list(x.max(axis=0)), nparray_to_list(x.max(axis=1)), float(x.max())]
    calculations['min'] = [nparray_to_list(x.min(axis=0)), nparray_to_list(x.min(axis=1)), float(x.min())]
    calculations['sum'] = [nparray_to_list(x.sum(axis=0)), nparray_to_list(x.sum(axis=1)), float(x.sum())]

    return calculations

def nparray_to_list(array):
    return np.array(array).tolist()