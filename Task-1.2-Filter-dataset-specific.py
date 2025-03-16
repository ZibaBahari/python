import numpy as np

def filter_dataset(dataset):
    rate = dataset[:,1].astype(float)
    
    filtered_dataset = dataset[rate == 8]
    print(filtered_dataset)
    return filtered_dataset
 
dataset =np.loadtxt('movies.csv' , delimiter=',', dtype=str,skiprows=1, encoding='utf-8')
filter_dataset(dataset)