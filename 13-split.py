import pandas as pd

dat = pd.read_csv('joined_data.csv')

size = len(dat)

split = int(3*(size/10))

dat = dat[:split]

dat.to_csv('Colab_sized_data')