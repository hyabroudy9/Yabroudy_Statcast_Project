# Hailey Yabroudy
# Project 3 Part 2
# Charting Data

# bar graph based on types of pitches
# which types of pitches has most movement
# which one is most popular
# need 'pitch_type_name', 'pitcher_break_z' and 'pitcher_break_x'

# z break is up and down
# x break is side to side

# find average of each pitch types movement for z and x

import csv
import matplotlib.pyplot as plt
import pandas as pd

data = open('pitch_movement.csv', newline='', encoding="utf-8")
df = pd.read_csv('pitch_movement.csv')


# add data to lists

# used this to find all of the pitch types in data
pitch = df["pitch_type_name"].to_list()
pitchcount = sorted(set(pitch), key=lambda x:pitch.index(x))

# i copied and pasted this from the output i got while making code
# pitchcount = ['4-Seamer', 'Sinker', 'Slider', 'Cutter', 'Changeup', 'Splitter', 'Curveball']


# go back through data and make pitches a critieriea for move append

# finding average z and x break for each pitch
# also putting these values into a dictionary
# source: https://stackoverflow.com/questions/40313727/bar-graph-from-dataframe-groupby
movement = df.groupby('pitch_type_name')['pitcher_break_z','pitcher_break_x'].mean().apply(list)
#print("The average z and x break for each pitch type is:")
#print(movement)


# create bar graph
p = movement.plot.bar()

plt.ylabel('Break in degrees')
plt.xlabel('Type of Pitch')
plt.xticks(rotation=0, fontsize=9)
plt.title("Type of Pitch by Break of Ball")

# to show values of each bar
# source: https://robertmitchellv.com/blog-bar-chart-annotations-pandas-mpl.html
for i in p.patches:
    p.text(i.get_x()+.04, i.get_height()+.5,\
           str(round((i.get_height()), 2)), fontsize=9)

plt.show()

# wanted to save image
plt.savefig('my_plot.png')



