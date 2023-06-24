import netflix as nf
from matplotlib import pyplot as plt

df = nf.df
z = df.groupby(["rating"]).size().reset_index(name='counts')
z = z[z["counts"] > 100].sort_values(by="counts")
pie_count = z["counts"]
pie_label = z["rating"]

plt.pie(pie_count,labels=pie_label,shadow = True,autopct='%.2f')

plt.legend(title = "Ratings",bbox_to_anchor=(1,0), loc="lower right",
                          bbox_transform=plt.gcf().transFigure)
plt.title("Rating pie chart")


plt.savefig("D:\\python\\New\\pythonProject\\MyWork\\Fif\\myplot")
plt.show()

