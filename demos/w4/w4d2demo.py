#W4D2 SEQUENTIAL SEARCH REVIEW / ADVANCED TEXT FILE HANDLING (CREATING / WRITING TO FILE)
#JOSHUA FRENCH
#
#PROMPT: In the W4D2 demo, we will review utilizing sequential search for simple singular and multi returns. We will then create and write data to a text file using Python.
#
#--IMPORTS---------------------------------------------------------------
import csv

#--FUNCTIONS-------------------------------------------------------------


#--MAIN CODE-------------------------------------------------------------

#create list for every potential field
dragons = []
riders = []
counts = []
color1 = []
color2 = [] #list filled only when count = 2

#--connected-------------------------------------------------------------
with open("textfiles/w4/dragons.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
       dragons.append(rec[0])
       riders.append(rec[1])
       counts.append(int(rec[2]))
       color1.append(rec[3])

       if int(rec[2]) == 2:
           color2.append(rec[4])
       elif int(rec[2]) == 1:
           color2.append("-----")
       else:
           color2.append("ERROR")
#--disconnected----------------------------------------------------------

#process lists to display data to console
print(f"{'DRAGONS':15}\t{'RIDERS':30}\t{'#':3}\t{'COLOR1':8}\t{'COLOR2':8}")
print("-----------------------------------------------------------------------------------------")

for i in range(0, len(dragons)):
    print(f"{dragons[i]:15}\t{riders[i]:30}\t{counts[i]:3}\t{color1[i]:8}\t{color2[i]:8}")
print("-----------------------------------------------------------------------------------------")

#SEARCH FOR SPECIFIC DRAGON
#step 1: set up
found = "x"
search = input("Which Dragon Are You Looking For?: ")

#step 2: perform search
for i in range(0, len(dragons)):
    if search.lower() in dragons[i].lower():
        found = i

#step 3: filter and display results
if found != "x":
    print(f"Your Search for {search} has Been Found: ")
    print(f"{dragons[found]:15}\t{riders[found]:30}\t{counts[found]:3}\t{color1[found]:8}\t{color2[found]:8}")
else:
    print(f"Your Search for {search} has NOT Been Found")

#SEARCH FOR COLOR SET AS A LIST VALUE
found = []
search = input("Which Color Are You Looking For?: ")

for i in range(0, len(color1)):
    if search.lower() in color1[i] or search.lower() in color2[i]:
        found.append(i)

if not found: #if found list is empty:
    print(f"Your Search for {search} has NOT Been Found")
else:
    print(f"Your Search for {search} has Been Found: ")
    for i in range(0, len(found)):
        print(f"{dragons[found[i]]:15}\t{riders[found[i]]:30}\t{counts[found[i]]:3}\t{color1[found[i]]:8}\t{color2[found[i]]:8}")

#CREATING A FILE
#create and write dragons and riders to new text file
file = open("textfiles/w4/targs.csv", "w")

for i in range(0, len(dragons)):
    file.write(f'{dragons[i]},{riders[i]}\n')
file.close()