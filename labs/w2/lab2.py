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
with open("labs/w2/csvs/filehandling.csv") as csvfile:
    file = csv.reader(csvfile)

    print(f"{"TYPE":10}{"BRAND":15}{"CPU":8}{"RAM":8}{"1ST DISK":12}{"NO HDD":8}{"2ND DISK":12}{"OS":8}{"YR":5}")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------")

    for rec in file:
        type = rec[0]
        if type == "D":
            type = "Desktop"
        elif type == "L":
            type = "Laptop"
        brand = rec[1]
        if brand == "DL":
            brand = "Dell"
        elif brand == "GW":
            brand = "Gateway"
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
        
    
        print(f"{type:10}{brand:15}{cpu:8}{ram:8}{disk1:12}{hdd:<8}{disk2:12}{os:8}{yr:5}")

