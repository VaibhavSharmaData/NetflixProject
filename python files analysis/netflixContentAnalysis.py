import netflix as nf
from matplotlib import pyplot as plt

plt.style.use('bmh')
df = nf.df




df1 = df[['type', 'release_year']]

df2 = df1.groupby(['release_year', 'type']).size().reset_index(name='Total Content')
df2 = df2[df2['release_year'] >= 2010]
year = list(df2["release_year"].unique())
x_tv = df2[df2["type"] == "TV Show"]["Total Content"]
x_M = df2[df2["type"] == "Movie"]["Total Content"]

plt.plot(year, x_tv)
plt.plot(year, x_tv, label = "TV")
plt.plot(year, x_M, label = "Movie")
plt.legend()
plt.tight_layout()
plt.savefig("D:\\python\\New\\pythonProject\\MyWork\\Fif\\content_analysis")
plt.show()