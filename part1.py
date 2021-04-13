# Hailey Yabroudy
# Project 3 Part 1
# Transforming Data

import csv
import pandas as pd

# read in csv file

data = open('pitch_movement.csv', newline='', encoding="utf-8")

# output contents into html page

# i'm going to be keeping all of the columns in the csv because i'm going to be
# using them for the chart

df = pd.read_csv('pitch_movement.csv')

df.to_html('pitchmove.html')
htmTable = df.to_html()

data.close()
