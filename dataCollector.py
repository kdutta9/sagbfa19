from populator import populate
from pandas import DataFrame

data = populate()

# change csv output to desired file name
df = DataFrame(data)
df.to_csv('output.csv')
