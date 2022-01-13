import sys
import os

clear = lambda: os.system('cls')
filename = input("Input Name of File (with extension) : ")
clear()
f= open(filename,"r")
f2= open("convert.txt","w+")
print("Get particle type from mythicmobs website : https://git.mythiccraft.io/mythiccraft/MythicMobs/-/wikis/skills/effects/particles/types")
particle = input("Input particle type : ")
clear()
i = 1
for x in f:
  if i >= 10:
    text = x.split()
    color = '#%02x%02x%02x' % (int(text[2]), int(text[3]), int(text[4]))
    positionz = text[6].replace("~","")
    positionx = text[8].replace("~","")
    speed = text[12]
    amount = text[13]
    f2.write("  - effect:particles{p="+particle+";color="+color+";forwardOffset="+positionz+";sideOffset="+positionx+";s="+speed+";a="+amount+"} @Self\n")
  elif i <= 9:
    i = i + 1
print("Complete the file ""convert.txt"" is now exist,\nPress any key to end.")
input()