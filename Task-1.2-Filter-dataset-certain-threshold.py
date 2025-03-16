import numpy as np

def filter_dataset(dataset):
    num_votes = dataset[:,2].astype(int)
    
    filtered_dataset = dataset[num_votes > 100]
    print(filtered_dataset)
    return filtered_dataset
 
dataset =np.loadtxt('movies.csv' , delimiter=',', dtype=str,skiprows=1, encoding='utf-8')
filter_dataset(dataset)