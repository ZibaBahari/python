import pandas as pd

def load_dataset(url):
    df = pd.read_csv(url, sep='\t')  # Load TSV
    df.to_csv('movies.csv', index=False)  # Save as CSV
    return "CSV file saved as movies.csv"

dataset_path = 'title.ratings.tsv'
print(load_dataset(dataset_path))