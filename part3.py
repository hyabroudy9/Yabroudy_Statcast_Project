# Hailey Yabroudy
# Project 3 Part 3
# Analyzing Data

import csv
import pandas as pd
import numpy as np

col_list = ['last_name',' first_name','team_name','pitch_hand','pitch_type_name','pitcher_break_z','pitcher_break_x']
data = open('pitch_movement.csv', newline='', encoding="utf-8")
df = pd.read_csv('pitch_movement.csv', usecols=col_list)
#final_df = df[['last_name','first_name','pitch_hand','pitch_type_name','pitcher_break_z','pitcher_break_x']]

# average z and x break for each pitch type

average = df.groupby('pitch_type_name')['pitcher_break_z','pitcher_break_x'].mean()
print("What is the average z and x break for each pitch type?")
print("The average z and x break for each pitch type is:")
print(average)

print('\n') # this just makes it easier to read all answers

# which pitch moves most vertically and horizontally
print("Which pitch moves the most vertically?")
ptchmostZ = df.groupby('pitch_type_name')['pitcher_break_z'].mean().nlargest(1)
print("The pitch with the highest average z break is:")
print(ptchmostZ)

print('\n')

print("Which pitch moves the most horizontally?")
ptchmostX = df.groupby('pitch_type_name')['pitcher_break_x'].mean().nlargest(1)
print("The pitch with the highest average x break is:")
print(ptchmostX)

print('\n')

# right handed or left handed pitchers get more movement?
handed = df.groupby('pitch_hand')['pitcher_break_z','pitcher_break_x'].mean()
print("Do right handed or left handed pitchers get more movement?")
print(handed)

print('\n')



# which pitch is most popular for right and left handed pitchers?
# source: https://stackoverflow.com/questions/40454030/count-and-sort-with-pandas
# source: https://www.youtube.com/watch?v=QAy89bQLjSU

fL = df['pitch_hand'] == 'L'
fR = df['pitch_hand'] == 'R'

popularL = df[fL].groupby(['pitch_type_name','pitch_hand'])['last_name']\
          .count() \
          .reset_index(name='number_pitchers') \
          .sort_values(['pitch_hand','number_pitchers'], ascending=False)
print("What are the most popular pitches ranked in order for left handed pitchers?")
print("The most popular pitches ranked in descending order:") 
print(popularL)

print('\n')

popularR = df[fR].groupby(['pitch_type_name','pitch_hand'])['last_name']\
          .count() \
          .reset_index(name='number_pitchers') \
          .sort_values(['pitch_hand','number_pitchers'], ascending=False)
print("What are the most popular pitches ranked in order for right handed pitchers?")
print("The most popular pitches ranked in descending order:")
print(popularR)


print('\n')

# source: https://stackoverflow.com/questions/42181022/selecting-the-first-row-of-a-sorted-group-from-pandas-data-frame
# which individual gets most movement vertically and horizontally?
indivZ = df.sort_values('pitcher_break_z', ascending=False)
print("Who gets the most movement vertically?")
print("The pitcher with the most vertical spin and the team he plays for is:")
print(indivZ.iloc[0,[1,0,2,4,5]])   

#print(indivZ)      # used this to verify who had the most

print('\n')

indivX = df.sort_values('pitcher_break_x', ascending=False)
print("Who gets the most movement horizontally?")
print("The pitcher with the most horizontal spin and the team he plays for is:")
print(indivX.iloc[0,[1,0,2,4,6]])  

#print(indivX)



        






