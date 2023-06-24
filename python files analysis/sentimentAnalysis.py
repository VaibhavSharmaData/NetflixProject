import netflix as nf
from matplotlib import pyplot as plt
from textblob import TextBlob  # for sentiment analysis
plt.style.use('ggplot')
df = nf.df


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
