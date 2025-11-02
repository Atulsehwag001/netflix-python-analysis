import pandas as pd
import matplotlib.pyplot as plt

# 1. load karo
df = pd.read_csv("netflix_titles.csv")

# 2. Count karo
type_count = df['type'].value_counts()

# 3. Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(type_count.values, labels=type_count.index, autopct='%1.1f%%', colors=['#ff6b6b', '#4ecdc4'], startangle=90)
plt.title("Netflix: Movies vs TV Shows", fontsize=16)

# 4. save kro
plt.savefig("netflix_movies_vs_tvshows.png", dpi=300, bbox_inches='tight')
plt.show()