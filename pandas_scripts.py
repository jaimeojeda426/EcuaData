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
pie_fig = px.pie(df2, values = 'Votes',names = 'Candidate', title = "Results")
bar_fig = px.bar(df2, x ="Candidate", y = "Votes")
#print(df) #default df created via dict
#print(df2) #df created via reading a csv
#both produce same df
pie_fig.show() #opens tab showing visualization
bar_fig.show()
#pie_fig.write_html("pie.html")
bar_fig.write_html("bar.html")

