import pandas as pd

def manipulate_dataset():
    dataset = pd.read_csv('title-genres.csv')
    print(dataset)
    
    dataset.head()
    
    dataset.tail()
    
    dataset.describe()
    
    dataset.info()
    
    return dataset
manipulate_dataset()