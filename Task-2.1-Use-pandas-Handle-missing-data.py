import pandas as pd

def manipulate_dataset():
    dataset = pd.read_csv('title-genres.csv')
    print(dataset)

    dataset.fillna(0, inplace=True)
    
    return dataset
manipulate_dataset()