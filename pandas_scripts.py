import pandas as pd

# Creating a DataFrame from a dictionary
# DataFrame - data structure that has the keys as it's column labels, and the values as data stored in those columns, has labeled axes for rows and columns
data = {
    'Candidate': ['D.Noboa', 'L.Gonzalez'],
    'Votes': [5870618, 4683260]
}
df = pd.DataFrame(data)
df2 = pd.read_csv('candidates - Sheet1.csv')
print(df)
print(df2)

