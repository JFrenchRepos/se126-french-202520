# Joshua French
# SE126.04
# FINAL LAB
#3-8-2025

# PROGRAM PROMPT: This program will read seating information from a CSV file, displaying the rows, seats, and their corresponding sections (e.g., Frontstage, VIP, Standard). Users will be prompted to enter the venue name, band name, ticket base price, and total band costs. At the end, it will display cost/profit statistics from the show.
# --IMPORTS--
import csv

# --CODE--
seats = [[], [], [], [], [], [], [], []]
with open("textfiles/w10/venue.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        for i in range(8):
            seats[i].append(rec[i])

print("---Show Information---")
venue = input("Enter the Name of the Venue: ").title()
band = input("Enter the Name of the Band Playing: ").title()
price = float(input("Enter the Standard Ticket Price (Affects Standard Price, Frontstage and VIP is Determined by Modifier): "))
modf = int(input("Enter Price Modifier Percentage for Frontstage Tickets (Calculated as Input/100): "))
modf = modf / 100
modv = int(input("Enter Price Modifier Percentage for VIP Tickets (Calculated as Input/100): "))
modv = modv / 100
cost = float(input("Enter the Total Costs for the Band: "))
rev = 0
netrev = 0
fcount = 0
vcount = 0
scount = 0

ans = "y"
while ans == "y":
    print(f"\nCurrently Available Seats for {band}'s show at {venue}:")
    print(f"{'ROWS:':5}\t{'SEATS:':5}\t{'SEATS:':5}\t{'SEATS:':5}\t{'SEATS:':5}\t{'SEATS:':5}\t{'SEATS:':5}\t{'TICKET:':10}")
    print("-" * 100)
    for i in range(len(seats[0])):
        print(f"{seats[0][i]:5}\t{seats[1][i]:5}\t{seats[2][i]:5}\t{seats[3][i]:5}\t{seats[4][i]:5}\t{seats[5][i]:5}\t{seats[6][i]:5}\t{seats[7][i]:10}")
    print("-" * 100)
    
    seatinput = input("Enter the seat you want to reserve (1A, 2B, 3C, etc): ")
    if len(seatinput) < 2:
        print("Invalid seat format. Please enter again.")
    else:
        rowpart = seatinput[:-1]
        seatpart = seatinput[-1].upper()

        validrow = True
        validseat = False

        if rowpart in [str(i) for i in range(1, len(seats[0]) + 1)]:
            rownum = int(rowpart)
        else:
            validrow = False

        if seatpart in ['A', 'B', 'C', 'D', 'E', 'F']:
            validseat = True
            seatindex = ['A', 'B', 'C', 'D', 'E', 'F'].index(seatpart) + 1

        if validrow and validseat:
            if seats[seatindex][rownum - 1] == 'X':
                print("Seat is occupied. Please choose another seat.")
            else:
                section = seats[7][rownum - 1].lower()
                if section == "frontstage":
                    ticketprice = price + (price * modf)
                    fcount += 1
                elif section == "vip":
                    ticketprice = price + (price * modv)
                    vcount += 1
                else:
                    ticketprice = price
                    scount += 1

                seats[seatindex][rownum - 1] = 'X'
                rev += ticketprice
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
print(f"{'ROWS:':5}\t{'SEATS:':5}\t{'SEATS:':5}\t{'SEATS:':5}\t{'SEATS:':5}\t{'SEATS:':5}\t{'SEATS:':5}\t{'TICKET:':10}")
print("-" * 100)
for i in range(len(seats[0])):
    print(f"{seats[0][i]:5}\t{seats[1][i]:5}\t{seats[2][i]:5}\t{seats[3][i]:5}\t{seats[4][i]:5}\t{seats[5][i]:5}\t{seats[6][i]:5}\t{seats[7][i]:5}")

netrev = rev - cost
print("-" * 75)
print(f"{band}'s Cost/Profit Analysis")
print(f"{'Base Ticket Price:':<50} ${price:>10.2f}")
print(f"{'Total Revenue from Ticket Sales:':<50} ${rev:>10.2f}")
print(f"{'Frontstage Tickets Sold:':<50} {fcount:>10}")
print(f"{'VIP Tickets Sold:':<50} {vcount:>10}")
print(f"{'Standard Tickets Sold:':<50} {scount:>10}")
print("-" * 75)
print(f"{f'Total Costs for {band}:':<50} ${cost:>10.2f}")
print(f"{'Net Revenue:':<50} ${netrev:>10.2f}")
print("-" * 75)