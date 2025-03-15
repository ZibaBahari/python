import numpy as np


def calculate_statistics():
    dataset =np.loadtxt('movies.csv' , delimiter=',', dtype=str,skiprows=1, encoding='utf-8')

    rating = dataset[:,1].astype(float)

    mean_rating = np.mean(rating)
    print("mean rating is ", mean_rating)

    median_rating = np.median(rating)
    print("median rating is ", median_rating)

    std_dev_rating =np.std(rating)
    print("standard deviation is ", std_dev_rating)
   



calculate_statistics()


