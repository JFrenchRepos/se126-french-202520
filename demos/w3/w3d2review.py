#W3D2 LIST REVIEW

#PROMPT: This demo will focus on reviewing accessing text file data and storing it in lists.

#--IMPORTS
import csv


#--FUNCTIONS



#--MAIN CODE

#initialize record counting var
totalrecs = 0

#creating empty list for all potential fields
first = []
last = []
g1 = []
g2 = []
g3 = []



#--connected to file
with open("demos/w3/csvs/class_grades.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        totalrecs += 1
        
        #store data from current record to corresponding lists with .append()
        
        #parallel lists --> data dispersed across lists, connected by same index
        first.append(rec[0])
        last.append(rec[1])
        g1.append(int(rec[2]))
        g2.append(int(rec[3]))
        g3.append(int(rec[4]))

#--disconnected from file

#processing lists (needs a for loop)
for index in range(0, len(first)):
    #for every item, index will start at 0 and run up to the # of items (len)
    print(f"INDEX {index}: {first[index]:10}\t{last[index]:10}\t{g1[index]:3}\t{g2[index]:3}\t{g3[index]:3}")

#new list to hold average test scores
avg = []

for i in range(0, len(g1)): #"i" is short for index
    a = (g1[i] + g2[i] + g3[i])/3
    avg.append(a)


print(f"\nINDEX: {'FIRST':10}\t{'LAST':10}\t{'G1':3}\t{'G2':3}\t{'G3':3}\t{'AVG'}")
print("------------------------------------------------------------------------------")
for index in range(0, len(first)):
    #for every item, index will start at 0 and run up to the # of items (len)
    print(f"INDEX {index}: {first[index]:10}\t{last[index]:10}\t{g1[index]:3}\t{g2[index]:3}\t{g3[index]:3}\t{avg[index]:.2f}")
print("------------------------------------------------------------------------------")

#calculation for total average
totalavg = 0
for i in range(0, len(avg)): #"i" is short for index
    totalavg += avg[i]

classavg = totalavg / len(avg)

print(f"\nTOTAL RECORDS: {totalrecs}\nCURRENT CLASS AVG: {classavg:.2f}")