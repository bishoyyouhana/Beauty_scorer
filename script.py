import os

os.chdir(r"C:\Users\Win8.1\source\repos\Beauty_scorer\training_ratings")
f = open("AM_ratings.txt","r")
line = f.read()

line = line.strip("\n")

f = open("AM_ratings.txt","w")

f.write(line)