#W2D1 = Text File Handling Intro Demo

#Step 1: import the csv library
import csv

totalrecords = 0 #holds total num of recs in file

#--connected to file-----
with open("demos/w2/csvs/simple.csv") as csvfile:
    file = csv.reader(csvfile)
    
    print(f"{"NAME":10}  {"NUM":3}    {"COLOR"}")
    print("---------------------------------------")

    for record in file:
        totalrecords += 1

        name = record[0]
        number = record[1]
        color = record[2]

        print(f"{name:10}  {number:3}    {color.title()}")


#--disconnected from file-----
print("---------------------------------------")
print(f"\nTOTAL RECORDS: {totalrecords}\n")