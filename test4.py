import pandas as pd

car_colors = pd.Series(['Blue', 'Red', 'Green'], dtype='category')
car_data = pd.Series(pd.Categorical(
    ['Blue', 'Green', 'Red', 'Green', 'Red', 'Green'],
    categories=car_colors, ordered=False))

car_data.cat.categories = ["Blue_Red", "Red", "Green"]

print(car_data.ix[car_data.isin(['Red'])])

car_data.ix[car_data.isin(['Red'])] = 'Blue_Red'

print(car_data)
