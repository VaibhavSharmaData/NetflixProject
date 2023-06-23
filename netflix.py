import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob


df = pd.read_csv("D:\\DATA\\netflix_titles.csv")
df.set_index("show_id", inplace=True)
pd.set_option('display.max_columns' , 10)