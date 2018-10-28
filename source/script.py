import os

f =open("ratings.txt","r")

content = f.read()

content = content.strip("\n")

f = open("ratings.txt","w")

f.write(content)

f.close()