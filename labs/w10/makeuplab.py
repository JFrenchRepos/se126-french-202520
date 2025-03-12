#Joshua French
#SE126.04
#LAB MAKEUP
#3-11-2025

#PROGRAM PROMPT: Makeup Lab
#IMPORTS-----------------------------------------------------------------------------------------------------------------------------------------------------------
import csv

def swap(index, listName):
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp

def menu():
    while True:
        print("\nSearch Menu")
        print("1. Show All Students")
        print("2. Search for a Student [ID]")
        print("3. Search for a Student [LAST]")
        print("4. View Class Roster")
        print("5. EXIT")
        menuchoice = input("Enter your choice: ")
        return menuchoice

#CODE--------------------------------------------------------------------------------------------------------------------------------------------------------------

id = []
lastnames = []
firstnames = []
class1 = []
class2 = []
class3 = []

with open("textfiles/w10/students.txt") as txtfile:
    file = csv.reader(txtfile)

    for rec in file:
        id.append(rec[0])
        lastnames.append(rec[1])
        firstnames.append(rec[2])
        class1.append(rec[3].title())
        class2.append(rec[4])
        class3.append(rec[5].title())

ans = "y"
while ans == "y":
    choice = menu()

    if choice == "1":
            for i in range(len(id) - 1):
                for j in range(len(id) - 1):
                    if id[j] > id[j + 1]:
                        swap(j, id)

            dex = list(range(len(id)))
            print(f"{'ID':10}\t{'Last':<32}\t{'First':30}\t{'Class 1':10}\t{'Class 2':10}\t{'Class 3':10}")
            print("--------------------------------------------------------------------------------------------------------------------------------------------")
            for i in dex:
                print(f"{id[mid]:10}\t{lastnames[mid]:<32}\t{firstnames[mid]:30}\t{class1[mid]:10}\t{class2[mid]:10}\t{class3[mid]:10}")
            print("--------------------------------------------------------------------------------------------------------------------------------------------")

    elif choice == "2":
            for i in range(len(id) - 1):
                for j in range(len(id) - 1):
                    if id[j] > id[j + 1]:
                        swap(j, id)

            search = input("Enter the Student ID you are looking for: ")

            min = 0
            max = len(id) - 1
            mid = int((min + max) / 2 )

            while min < max and search.lower() != id[mid].lower():
                if search.lower() < id[mid].lower():
                    max = mid - 1
                else:
                    min = mid + 1

                mid = int((min + max) / 2 )
    
            if search.lower() == id[mid].lower():
                print(f"\nFound {search}: ")
                print(f"{'ID':10}\t{'Last':<32}\t{'First':30}\t{'Class 1':10}\t{'Class 2':10}\t{'Class 3':10}")
                print(f"\n--------------------------------------------------------------------------------------------------------------------------------------------")
                print(f"{id[mid]:10}\t{lastnames[mid]:<32}\t{firstnames[mid]:30}\t{class1[mid]:10}\t{class2[mid]:10}\t{class3[mid]:10}")
                print("--------------------------------------------------------------------------------------------------------------------------------------------\n")
            else:
                print("No results found!")

    elif choice == "3":
            for i in range(len(lastnames) - 1):
                for j in range(len(lastnames) - 1):
                    if lastnames[j] > lastnames[j + 1]:
                        swap(j, lastnames)

            search = input("Enter the Student's Last Name you are looking for: ")
            min = 0
            max = len(lastnames) - 1
            mid = int((min + max) / 2 )

            while min < max and search.lower() != lastnames[mid].lower():
                if search.lower() < lastnames[mid].lower():
                    max = mid - 1
                else:
                    min = mid + 1

                mid = int((min + max) / 2 )
    
            if search.lower() == lastnames[mid].lower():
                print(f"\nFound {search}: ")
                print(f"{'ID':10}\t{'Last':<32}\t{'First':30}\t{'Class 1':10}\t{'Class 2':10}\t{'Class 3':10}")
                print(f"\n--------------------------------------------------------------------------------------------------------------------------------------------")
                print(f"{id[mid]:10}\t{lastnames[mid]:<32}\t{firstnames[mid]:30}\t{class1[mid]:10}\t{class2[mid]:10}\t{class3[mid]:10}")
                print("--------------------------------------------------------------------------------------------------------------------------------------------\n")
            else:
                print("No results found!")

    elif choice == "4":
            found = []
            search = input("Enter the Class you are looking for: ")
            for i in range(0, len(class1)):
                if search.lower() in class1[i].lower() or search.lower() in class2[i].lower() or search.lower() in class3[i].lower():
                    found.append(i)

            if not found:
                print("No results found!")
            else:
                print(f"\nFound {search}: ")
                print(f"{'ID':10}\t{'Last':<32}\t{'First':30}\t{'Class 1':10}\t{'Class 2':10}\t{'Class 3':10}")
                print(f"\n--------------------------------------------------------------------------------------------------------------------------------------------")
                for i in range(0, len(found)):
                     print(f"{id[found[i]]:10}\t{lastnames[found[i]]:<32}\t{firstnames[found[i]]:30}\t{class1[found[i]]:10}\t{class2[found[i]]:10}\t{class3[found[i]]:10}")
                
                print("--------------------------------------------------------------------------------------------------------------------------------------------\n")
  
            
    elif choice == "5":
            print("Goodbye!")
            ans = "x"

    else:
            print("Invalid choice!")
