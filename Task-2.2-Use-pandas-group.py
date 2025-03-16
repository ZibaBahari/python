import pandas as pd

def group_dataset():
    dataset = pd.read_csv('title-genres.csv')
    print(dataset)


    group =  dataset.groupby('genres')

    for name, group in group:
        print(name)
        print(group)
        

    

    
    return group
print(group_dataset())