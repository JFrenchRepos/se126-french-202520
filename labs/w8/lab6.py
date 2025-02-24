#Joshua French
#SE126.04
#LAB 6
#2-20-2025

#PROGRAM PROMPT: Write a Python program using lists (1D or 2D) to assign passengers seats in an airplane.
#--IMPORTS--
import csv



#--CODE--
row1 = []
row2 = []
row3 = []
row4 = []
row5 = []

seatA = []

with open("textfiles/w8/seats.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        row1.append(rec[0])
        row2.append(rec[1])
        row3.append(rec[2])
        row4.append(rec[3])
        row5.append(rec[4])

print(f"\nCurrently Available Seats:")
print(f"{'ROWS':5}\t{'SEATS':5}")
print("-----------------------------------------------------------------------")
for i in range(0, len(row1)):
    print(f"{row1[i]:5}\t{row2[i]:5}\t{row3[i]:10}\t{row4[i]:5}\t{row5[i]:5}\n")

ans = "y"
while ans == "y":
    prompt = input("Start seat reservation?: ")
    if prompt == 'y':
        rowprompt = int(input("Which row did you want to search?: "))
        if rowprompt == 1:
            seat = input("Which seat did you want to reserve?: ")
            if seat.lower() == "A":
                if seatA(rowprompt - 1) != 'x':
                    seatA(rowprompt - 1) == 'x'
                else:
                    print("This seat is unavailable")

            

            
                        



    else:
        ans = "n"
    
