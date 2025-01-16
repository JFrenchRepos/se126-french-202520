#Joshua French
#SE126.04
#LAB 2
#1-16-2025

#PROGRAM PROMPT: This is a program to produce a report that lists all the computers in the csv file filehandling.csv.

#VARIABLE DICTIONARY
#-------------------------------------------------------------------------------------------------------------------------------------------------#
#IMPORTS------------------------------------------------------------------------------------------------------------------------------------------#
import csv

#---connected to file-----------------------------------------------------------------------------------------------------------------------------#
totalrec = 0

with open("labs/w2/csvs/filehandling.csv") as csvfile:
    file = csv.reader(csvfile)

    print(f"{"TYPE":20}{"BRAND":20}{"CPU":20}{"RAM":20}{"1ST DISK":20}{"NO HDD":20}{"2ND DISK":20}{"OS":20}{"YR":20}")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------")

    for rec in file:
        totalrec += 1

        type = rec[0]
        brand = rec[1]
        cpu = rec[2]
        ram = rec[3]
        disk1 = rec[4]
        hdd = int(rec[5])

        if hdd == 2:
            disk2 = rec[6]
            os = rec[7]
            yr = rec[8]
        else:
            disk2 = "-----"
            os = rec[6]
            yr = rec[7]
        
    
        print(f"{type:20}{brand:20}{cpu:20}{ram:20}{disk1:20}{hdd:20}{disk2:20}{os:20}{yr:20}")

