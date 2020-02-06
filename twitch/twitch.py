import sqlite3
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import os.path

os.chdir("/Users/131093/development/git/python/codecademy-projects/twitch/")
print(os.path.abspath('dev.db')) 
BASE_DIR = os.path.dirname(os.path.abspath('dev.db'))
db_path = os.path.join(BASE_DIR, "dev.db")
cnx = sqlite3.connect(db_path)

df = pd.read_sql_query("SELECT * FROM top_games_jan_1_2015", cnx)
games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]
viewers = df['viewers']

print(games)
print(viewers)

plt.bar(range(len(games)), viewers, color='#644185')
plt.title('Featured Games Viewers')
plt.xlabel('Games')
plt.ylabel('Viewers')
plt.legend(['Twitch'])

ax = plt.subplot()
ax.set_xticks([0,1,2,3,4,5,6,7,8,9,10])
ax.set_xticklabels(games, rotation=30)

plt.show()

plt.clf()