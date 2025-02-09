#Joshua French
#SE126.04
#LAB 4
#1-30-2025

#PROGRAM PROMPT: This is a two-part program where you will work on creating and populating parallel lists based on file data, then create and write data to a file.
#IMPORTS-----------------------------------------------------------------------------------------------------------------------------------------------------------
import csv

#CODE--------------------------------------------------------------------------------------------------------------------------------------------------------------
first = []
last = []
age = []
sname = []
house = []

emails = []
departments = []
phone = []

phone_counters = {
    "House Stark": 100,
    "House Targaryen": 200,
    "House Tully": 300,
    "House Lannister": 400,
    "House Baratheon": 500,
    "The Night's Watch": 600
}

#--connected to file--
with open("textfiles/w4/got_emails.csv", newline='') as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        first.append(rec[0])
        last.append(rec[1])
        age.append(int(rec[2]))
        sname.append(rec[3])
        house.append(rec[4])

        email = rec[3] + "@westeros.net"
        emails.append(email)

        if rec[4] == "House Stark":
            departments.append("Research & Development")
            phone.append(phone_counters["House Stark"])
            phone_counters["House Stark"] += 1

        elif rec[4] == "House Targaryen":
            departments.append("Marketing")
            phone.append(phone_counters["House Targaryen"])
            phone_counters["House Targaryen"] += 1

        elif rec[4] == "House Tully":
            departments.append("Human Resources")
            phone.append(phone_counters["House Tully"])
            phone_counters["House Tully"] += 1

        elif rec[4] == "House Lannister":
            departments.append("Accounting")
            phone.append(phone_counters["House Lannister"])
            phone_counters["House Lannister"] += 1

        elif rec[4] == "House Baratheon":
            departments.append("Sales")
            phone.append(phone_counters["House Baratheon"])
            phone_counters["House Baratheon"] += 1

        elif rec[4] == "The Night's Watch":
            departments.append("Auditing")
            phone.append(phone_counters["The Night's Watch"])
            phone_counters["The Night's Watch"] += 1

        else:
            departments.append("-----")
            phone.append("-----")

#--disconnected from file--
print(f"{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':3}")
for i in range(0, len(first)):
    print(f"{first[i]:8} {last[i]:10} {emails[i]:30} {departments[i]:23} {phone[i]:3}")

file = open("westeros.csv", 'w')
for i in range(0, len(first)):

    file.write(f'{first[i]}, {last[i]}, {emails[i]}, {departments[i]}, {phone[i]}\n')
file.close()

print(f"\nFile 'westeros.csv' created successfully with {len(first)} employees.")

department_counts = {}
for dept in departments:
    if dept in department_counts:
        department_counts[dept] += 1
    else:
        department_counts[dept] = 1

print("\nEmployee count per department:")
for dept, count in department_counts.items():
    print(f"{dept}: {count}")