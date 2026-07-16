import pandas as pd
import plotly.express as px


# Creating a DataFrame from a dictionary
# DataFrame - data structure that has the keys as it's column labels, and the values as data stored in those columns, has labeled axes for rows and columns
data = {
    'Candidate': ['D.Noboa', 'L.Gonzalez'],
    'Votes': [5870618, 4683260]
}
df = pd.DataFrame(data)
df2 = pd.read_csv('candidates - Sheet1.csv')
pie_fig = px.pie(df, values = 'Votes',names = 'Candidate', title = "Results")
#print(df) #default df created via dict
#print(df2) #df created via reading a csv
#both produce same df
pie_fig.show()

