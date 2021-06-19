import pandas as pd


data = pd.DataFrame({
    'city': ['auckland', 'berlin', 'london'],
    'population': [1.6, 3.6, 8.9],
    'hemisphere': ['south', 'north', 'north'],
    'land-area': [1086, 891, 1572]
  })
data.to_csv('./cities/cities.csv')
