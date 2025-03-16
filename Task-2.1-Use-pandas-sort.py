import pandas as pd

def sort_dataset():
    dataset = pd.read_csv('title-genres.csv')
    print(dataset)


    dataset.sort_values(by=['startYear'], ascending=False, inplace=True)
    
    return dataset
print(sort_dataset())