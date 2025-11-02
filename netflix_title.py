# Netflix Top 10 Countries
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")
top_countries = df['country'].value_counts().head(10)

plt.figure(figsize=(8,6))
top_countries.plot(kind='bar', color='red')
plt.title("Top 10 Countries by Netflix Content", fontsize=16)
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=90)
plt.savefig("netflix_top_countries.png")

plt.show()
