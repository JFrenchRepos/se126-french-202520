#Joshua French
#SE126.04
#LAB 4
#1-30-2025

#PROGRAM PROMPT: This is a two-part program where you will work on creating and populating parallel lists based on file data, then create and write data to a file.
#IMPORTS-----------------------------------------------------------------------------------------------------------------------------------------------------------
import csv

#CODE--------------------------------------------------------------------------------------------------------------------------------------------------------------
first = []
last = []
age = []
sname = []
house = []

#--connected-------------------------------------------------------------------------------------------------------------------------------------------------------
with open("textfiles/w4/got_emails.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        first.append(rec[0])
        last.append(rec[1])
        age.append(int(rec[2]))
        sname.append(rec[3])
        house.append(rec[4])
#--disconnected----------------------------------------------------------------------------------------------------------------------------------------------------
