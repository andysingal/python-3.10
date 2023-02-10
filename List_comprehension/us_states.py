import pandas as pd
from pprint import pprint
import csv
# with open('weather_data.csv') as f:
#     content = csv.reader(f)
#     temperature = []
#     for row in content:
#         if row[1] != 'temp':
#             temperature.append(row[1])
#     print(temperature)
df = pd.read_csv('weather_data.csv')
print(df.head())
df.temp = df.temp.astype(int)
temp_list = df["temp"].to_list()
avg = sum(df["temp"])/len(df["temp"])
print(avg)
monday = df[df.day == 'Monday']['temp']
print(monday)





