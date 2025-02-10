#Joshua French
#SE126.04
#MIDTERM
#2-10-2025

#PROGRAM PROMPT: Using the file named above, read the data from the file and store to 1D parallel lists. Once the lists have been fully populated with file data, create a new list to hold an office number for each of the employees. Office numbers should start at 100 and not exceed 200. Assign each employee an office number and store to the newly created list, then process through the six lists to display all of the data to the user as well as the total number of records in the file. 

#IMPORTS------------------------------------------------------------------------------------------
import csv

#CODE
first = []
last = []
email = []
dept = []
phone = []
office = []

officenum = {
    "Research & Development": 100,
    "Auditing": 120,
    "Human Resources": 140,
    "Accounting": 160,
    "Sales": 180,
    "Marketing": 199
}

#--connected to file--
with open("textfiles/w6/westeros.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        first.append(rec[0])
        last.append(rec[1])
        email.append(rec[2])
        dept.append(rec[3])
        if rec[3] == "Research & Development":
            office.append(officenum["Research & Development"])
            officenum["Research & Development"] += 1
        
        elif rec[3] == "Auditing":
            office.append(officenum["Auditing"])
            officenum["Auditing"] += 1
        
        elif rec[3] == "Human Resources":
            office.append(officenum["Human Resources"])
            officenum["Human Resources"] += 1

        elif rec[3] == "Accounting":
            office.append(officenum["Accounting"])
            officenum["Accounting"] += 1

        elif rec[3] == "Sales":
            office.append(officenum["Sales"])
            officenum["Sales"] += 1

        elif rec[3] == "Marketing":
            office.append(officenum["Marketing"])
            officenum["Marketing"] += 1
        phone.append(rec[4])


#--disconnected from file--

#--display--
print(f"{'FIRST':8}\t{'LAST':8}\t{'EMAIL':30}\t{'DEPT':20}\t{'OFFICE':3}\t{'EXT':3}")
print("----------------------------------------------------------------------------------------------------------------------------------")
for i in range(0, len(first)):
    print(f"{first[i]:8}\t{last[i]:8}\t{email[i]:30}\t{dept[i]:20}\t{office[i]:3}\t{phone[i]:3}")
print("----------------------------------------------------------------------------------------------------------------------------------")

file = open("midterm_choice1.csv", "w")
for i in range(0, len(first)):
    file.write(f"{first[i]:8}\t{last[i]:8}\t{email[i]:30}\t{dept[i]:20}\t{office[i]:3}\t{phone[i]:3}\n")
file.close()

print(f"\nFile 'midterm_choice1.csv' has been created.")

#--search--
found = "x"

print("-------------")
print("1. EMAIL")
print("2. DEPARTMENT")
print("3. EXIT")
print("-------------")
prompt = input("Choose a Number to Begin the Search: ")
while prompt != "1" and prompt != "2" and prompt != "3":
    print("Invalid Input")
    print("-------------")
    print("1. EMAIL")
    print("2. DEPARTMENT")
    print("3. EXIT")
    print("-------------")
    prompt = input("Choose a Number to Begin the Search: " )

while prompt == "1" or prompt == "2":
    if prompt == "1":
        search = input("Which Email Did You Want to Search for?: ")
        for i in range(0, len(email)):
            if search in email[i].lower():
                found = i
    
        if found != "x":
            print("----------------------------------------------------------------------------------------------------------------------------------")
            print(f"Your Search for {search} has been Found: ")
            print(f"{'FIRST':8}\t{'LAST':8}\t{'EMAIL':30}\t{'DEPT':20}\t{'OFFICE':3}\t{'EXT':3}")
            print("----------------------------------------------------------------------------------------------------------------------------------")
            print(f"{first[found]:8}\t{last[found]:8}\t{email[found]:30}\t{dept[found]:20}\t{office[found]:3}\t{phone[found]:3}")
            print("----------------------------------------------------------------------------------------------------------------------------------")
            print("-------------")
            print("1. EMAIL")
            print("2. DEPARTMENT")
            print("3. EXIT")
            print("-------------")
            prompt = input("Choose a Number to Begin the Search: ")
            while prompt != "1" and prompt != "2" and prompt != "3":
                print("Invalid Input")
                print("-------------")
                print("1. EMAIL")
                print("2. DEPARTMENT")
                print("3. EXIT")
                print("-------------")
                prompt = input("Choose a Number to Begin the Search: " )

        else:
            print(f"Your Search for {search} has NOT been Found")
            print("-------------")
            print("1. EMAIL")
            print("2. DEPARTMENT")
            print("3. EXIT")
            print("-------------")
            prompt = input("Choose a Number to Begin the Search: ")
            while prompt != "1" and prompt != "2" and prompt != "3":
                print("Invalid Input")
                print("-------------")
                print("1. EMAIL")
                print("2. DEPARTMENT")
                print("3. EXIT")
                print("-------------")
                prompt = input("Choose a Number to Begin the Search: " )

    elif prompt == "2":
        found = []
        search = input("Which Department Did You Want to Search for?: ")
        for i in range(0, len(dept)):
            if search in dept[i].lower():
                found.append(i)
    
        if not found:
            print(f"Your Search for {search} has NOT been Found")
            print("-------------")
            print("1. EMAIL")
            print("2. DEPARTMENT")
            print("3. EXIT")
            print("-------------")
            prompt = input("Choose a Number to Begin the Search: ")
            while prompt != "1" and prompt != "2" and prompt != "3":
                print("Invalid Input")
                print("-------------")
                print("1. EMAIL")
                print("2. DEPARTMENT")
                print("3. EXIT")
                print("-------------")
                prompt = input("Choose a Number to Begin the Search: " )

        else:
            print("----------------------------------------------------------------------------------------------------------------------------------")
            print(f"Your Search for {search} has been Found: ")
            for i in range(0, len(found)):
                print(f"{'FIRST':8}\t{'LAST':8}\t{'EMAIL':30}\t{'DEPT':20}\t{'OFFICE':3}\t{'EXT':3}")
                print("----------------------------------------------------------------------------------------------------------------------------------")
                print(f"{first[found[i]]:8}\t{last[found[i]]:8}\t{email[found[i]]:30}\t{dept[found[i]]:20}\t{office[found[i]]:3}\t{phone[found[i]]:3}")
            print("----------------------------------------------------------------------------------------------------------------------------------")
            print("-------------")
            print("1. EMAIL")
            print("2. DEPARTMENT")
            print("3. EXIT")
            print("-------------")
            prompt = input("Choose a Number to Begin the Search: ")
            while prompt != "1" and prompt != "2" and prompt != "3":
                print("Invalid Input")
                print("-------------")
                print("1. EMAIL")
                print("2. DEPARTMENT")
                print("3. EXIT")
                print("-------------")
                prompt = input("Choose a Number to Begin the Search: " )

print("Goodbye!")


