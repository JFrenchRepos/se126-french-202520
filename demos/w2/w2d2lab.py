#W2D2 - Text File Handling Review
#1-16-25
#Joshua French

#PROMPT:

#VAR DICTIONARY:

#IMPORTS---------------------------------------------------------------------------
import csv


#FUNCTIONS-------------------------------------------------------------------------
def difference(ppl, max):
    #this function is passed 2 values and returns the difference between the 2
    diff = max - ppl
    return diff

#MAIN CODE-------------------------------------------------------------------------

#initialize counting vars
totalrec = 0
roomsover = 0

#---connected to file--------------------------------------------------------------
with open("demos/w2/csvs/classLab2.csv") as csvfile:
    file = csv.reader(csvfile)

    print(f"{"NAME":20}  {"MAX":5}   {"PPL":5}   {"REM":5}")
    print("-----------------------------------------------")
    for rec in file:
        #code executes for every record in file
        #assign each field data value to a friendly var name
        name = rec[0]
        max = int(rec[1])   #all text data is read as a string unless otherwise specified (int)
        ppl = int(rec[2])

        #call difference()
        rem = difference(ppl, max)

        #count and display over capacity rooms
        if rem < 0:
            roomsover += 1
            print(f"{name:20}  {max:5}   {ppl:5}   {abs(rem):5}")

        #count all rooms
        totalrec += 1






#---disconnected from file---------------------------------------------------------
print(f"\nRooms currently over capacity: {roomsover}")
print(f"\nRooms stored in file: {totalrec}")