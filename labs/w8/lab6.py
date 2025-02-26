# Joshua French
# SE126.04
# LAB 6
# 2-20-2025

# PROGRAM PROMPT: Write a Python program using lists (1D or 2D) to assign passengers seats in an airplane.
# --IMPORTS--
import csv

# --CODE--
rows = [[], [], [], [], []]

with open("textfiles/w8/seats.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        for i in range(5):
            rows[i].append(rec[i])

ans = "y"
while ans == "y":
    print("\nCurrently Available Seats:")
    print(f"{'ROWS:':5}\t{'SEATS:':5}")
    print("-----------------------------------------------------------------------")
    for i in range(len(rows[0])):
        print(f"{rows[0][i]:5}\t{rows[1][i]:5}\t{rows[2][i]:10}\t{rows[3][i]:5}\t{rows[4][i]:5}")

    seatinput = input("Enter the seat you want to reserve (1A, 2B, 3C, etc): ")

    if len(seatinput) < 2:
        print("Invalid seat format. Please enter again.")
    else:
        rowpart = seatinput[:-1]
        seatpart = seatinput[-1].upper()

        validrow = True
        validseat = False

        if rowpart in [str(i) for i in range(1, len(rows[0]) + 1)]:
            rownum = int(rowpart)
        else:
            validrow = False

        if seatpart in ['A', 'B', 'C', 'D']:
            validseat = True
            seatindex = ['A', 'B', 'C', 'D'].index(seatpart) + 1

        if validrow and validseat:
            if rows[seatindex][rownum - 1] == 'X':
                print("Seat is occupied. Please choose another seat.")
            else:
                rows[seatindex][rownum - 1] = 'X'
                validinput = False
                while not validinput:
                    ans = input("Do you want to continue reserving seats? (y/n): ").lower()
                    if ans in ['y', 'n']:
                        validinput = True
                    else:
                        print("Invalid input. Try again")
        else:
            print("Invalid seat number or letter. Please enter again.")

print("Final seating arrangement:")
print(f"{'ROWS:':5}\t{'SEATS:':5}")
print("-----------------------------------------------------------------------")
for i in range(len(rows[0])):
    print(f"{rows[0][i]:5}\t{rows[1][i]:5}\t{rows[2][i]:10}\t{rows[3][i]:5}\t{rows[4][i]:5}")


    
