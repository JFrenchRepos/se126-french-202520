#Joshua French
#SE126.04
#LAB 3
#1-23-2025

#PROGRAM PROMPT: This is a program that will analyze potential voters.
#IMPORTS------------------------------------------------------------------------------------------------------------------------------------------#
import csv

cregister = 0
nregister = 0
nvote = 0
voters = 0
totalrec = 0
#CODE---------------------------------------------------------------------------------------------------------------------------------------------#
id = []
age = []
reg = []
vote = []

#--connected to file
with open ("labs/w3/csvs/voters_202040.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        totalrec +=1

        id.append(rec[0])
        age.append(int(rec[1]))
        reg.append(rec[2])
        vote.append(rec[3])


#--disconnected from file
print(f"\nINDEX: {"ID":10}\t{"AGE":3}\t{"REG":3}\t{"CAN VOTE":3}")
print("------------------------------------------------")
for i in range(0, len(id)):
    while age[i] < 18:
        cregister += 1

    while reg[i] == "N":
        nregister += 1

    if vote[i] == "Y":
        voters += 1
    else:
        nvote += 1

    print(f"INDEX {i}: {id[i]:10}\t{age[i]:3}\t{reg[i]:3}\t{vote[i]:3}")
print("------------------------------------------------")

