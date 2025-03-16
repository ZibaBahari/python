import numpy as np

def calculate_numerical():
    dataset =np.loadtxt('movies.csv' , delimiter=',', dtype=str,skiprows=1, encoding='utf-8')
    print(dataset)
    
    num_votes = dataset[:,2].astype(int)

    max_num_votes = np.max(num_votes)
    print("max number of votes is ", max_num_votes)

    min_num_votes = np.min(num_votes)
    print("min number of votes is ", min_num_votes)

    mean_num_votes = np.mean(num_votes)
    print("mean number of votes is ", mean_num_votes)

    median_num_votes = np.median(num_votes)
    print("median number of votes is ", median_num_votes)

    std_dev_num_votes = np.std(num_votes)
    print("standard deviation is ", std_dev_num_votes)  
    

calculate_numerical()    