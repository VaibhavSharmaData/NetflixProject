import netflix as nf
from matplotlib import pyplot as plt

plt.style.use('bmh')
df = nf.df

df['director'] = df['director'].fillna('No Director Specified')
new_df_director = df['director'].str.split(',', expand=True).stack().to_frame()
new_df_director.columns = ["Director"]
directors = new_df_director.groupby(['Director']) \
    .size().reset_index(name='Total Content')
directors = directors[directors.Director != 'No Director Specified']
directors = directors.sort_values(by='Total Content', ascending=False).head().sort_values(by = 'Total Content')
people = directors['Director']
y = directors['Total Content']
plt.barh(people,y, height=0.40)
plt.title("Top 5 Directors on Netflix")
plt.tight_layout()
plt.savefig("D:\\python\\New\\pythonProject\\MyWork\\Fif\\top5directors")
plt.show()