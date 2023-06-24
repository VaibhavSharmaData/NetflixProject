import netflix as nf
from matplotlib import pyplot as plt

plt.style.use('ggplot')
df = nf.df

df['cast'] = df['cast'].fillna('No Actors Specified')
cast = df['cast'].str.split(',', expand=True).stack().to_frame()
cast.columns = ["cast"]
cast = cast[cast["cast"] != "No Actors Specified"]
castn = cast.groupby(['cast']).size().reset_index(name='Total movie')
castn = castn.sort_values(by="Total movie", ascending=False).head().sort_values(by = 'Total movie')


x_act = castn["cast"]
y_act = castn["Total movie"]

plt.barh(x_act,y_act,height=0.40)

plt.title("Top 5 Actors on Netflix")
plt.tight_layout()
plt.savefig("D:\\python\\New\\pythonProject\\MyWork\\Fif\\top5Actors")
plt.show()
