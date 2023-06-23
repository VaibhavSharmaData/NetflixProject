# importing data analysis packages

import numpy as np  # linear algebra
import pandas as pd  # for data preparation
import plotly.express as px  # for data visualization
import matplotlib.pyplot as plt
from textblob import TextBlob  # for sentiment analysis


pd.set_option('display.max_columns' , 10)
plt.style.use("fivethirtyeight")



# Top 5 Actors and Directors:
# Now let’s see the top 5 successful directors on this platform:
df['director'] = df['director'].fillna('No Director Specified')
new_df_director = df['director'].str.split(',', expand=True).stack().to_frame()
new_df_director.columns = ["Director"]
directors = new_df_director.groupby(['Director']) \
    .size().reset_index(name='Total Content')
directors = directors[directors.Director != 'No Director Specified']
directors = directors.sort_values(by='Total Content', ascending=False).head()
people = directors['Director']
y = directors['Total Content']
# plt.barh(people,y)
# # plt.show()

# end of this block of code
# ------------------------------------------------------------------------------
# Now let’s have a look at the top 5 successful actors on this platform:

df['cast'] = df['cast'].fillna('No Actors Specified')
cast = df['cast'].str.split(',', expand=True).stack().to_frame()
cast.columns = ["cast"]
cast = cast[cast["cast"] != "No Actors Specified"]
castn = cast.groupby(['cast']).size().reset_index(name='Total movie')
castn = castn.sort_values(by="Total movie", ascending=False).head()
# print(castn)

x_act = castn["cast"]
y_act = castn["Total movie"]

# plt.barh(x_act,y_act)
# plt.show()
# --====================================-------


# Analyzing Content on Netflix:
# The next thing to analyze from this data is
# the trend of production over the years on Netflix:

df1 = df[['type', 'release_year']]

df2 = df1.groupby(['release_year', 'type']).size().reset_index(name='Total Content')
df2 = df2[df2['release_year'] >= 2010]
year = list(df2["release_year"].unique())
x_tv = df2[df2["type"] == "TV Show"]["Total Content"]
x_M = df2[df2["type"] == "Movie"]["Total Content"]

# plt.plot(year, x_tv)
# plt.plot(year, x_tv, label = "TV")
# plt.plot(year, x_M, label = "Movie")
# plt.legend()
# plt.tight_layout()
# plt.show()

# At last, to conclude our analysis,
# I will analyze the sentiment of content on Netflix:
def sent(a):
    if (a == 0):
        return "Neutral"
    elif (a > 0):
        return "Positive"
    else:
        return "Negative"




dfx=df[['release_year','description']]

for index,row in dfx.iterrows():
    test = TextBlob(row["description"])
    p = test.sentiment.polarity
    dd = sent(p)
    print(dd)
    dfx['Sentiment'] = dd




print(dfx)
