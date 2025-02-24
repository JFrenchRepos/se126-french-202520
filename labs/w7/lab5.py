#Joshua French
#SE126.04
#LAB 5
#1-30-2025

#PROGRAM PROMPT: Build a personal library search system using the file book_list.csv.
#IMPORTS-----------------------------------------------------------------------------------------------------------------------------------------------------------
import csv

def swap(index, listName):
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp

def menu():
    while True:
        print("\nLibrary Menu")
        print("1. Show All Titles")
        print("2. Search by Title")
        print("3. Search by Author")
        print("4. Search by Genre")
        print("5. Search by Library Number")
        print("6. Show All Available")
        print("7. Show All On Loan")
        print("8. EXIT")
        menuchoice = input("Enter your choice: ")
        return menuchoice

#CODE--------------------------------------------------------------------------------------------------------------------------------------------------------------

libraries = []
titles = []
authors = []
genres = []
pages = []
statuses = []

with open("textfiles/w7/book_list.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        libraries.append(rec[0])
        titles.append(rec[1])
        authors.append(rec[2])
        genres.append(rec[3].title())
        pages.append(rec[4])
        statuses.append(rec[5].title())

ans = "y"
while ans == "y":
    choice = menu()

    if choice == "1":
            for i in range(len(titles) - 1):
                for j in range(len(titles) - 1):
                    if titles[j] > titles[j + 1]:
                        swap(j, titles)

            dex = list(range(len(titles)))
            print(f"{'Library Number':10}\t{'Title':<32}\t{'Author':30}\t{'Genre':30}\t{'Pages':5}\t{'Status':10}")
            print("--------------------------------------------------------------------------------------------------------------------------------------------")
            for i in dex:
                print(f"{libraries[i]:10}\t{titles[i]:<32}\t{authors[i]:30}\t{genres[i]:30}\t{pages[i]:5}\t{statuses[i]:10}")
            print("--------------------------------------------------------------------------------------------------------------------------------------------")

    elif choice == "2":
            for i in range(len(titles) - 1):
                for j in range(len(titles) - 1):
                    if titles[j] > titles[j + 1]:
                        swap(j, titles)

            search = input("Enter the Title you are looking for: ")

            min = 0
            max = len(titles) - 1
            mid = int((min + max) / 2 )

            while min < max and search.lower() != titles[mid].lower():
                if search.lower() < titles[mid].lower():
                    max = mid - 1
                else:
                    min = mid + 1

                mid = int((min + max) / 2 )
    
            if search.lower() == titles[mid].lower():
                print(f"\nFound {search}: ")
                print(f"{'Library Number':10}\t{'Title':<32}\t{'Author':30}\t{'Genre':30}\t{'Pages':5}\t{'Status':10}")
                print(f"\n--------------------------------------------------------------------------------------------------------------------------------------------")
                print(f"{libraries[mid]:10}\t{titles[mid]:<32}\t{authors[mid]:30}\t{genres[mid]:30}\t{pages[mid]:5}\t{statuses[mid]:10}")
                print("--------------------------------------------------------------------------------------------------------------------------------------------\n")
            else:
                print("No results found!")

    elif choice == "3":
            found = []
            search = input("Enter the Author you are looking for: ")
            for i in range(0, len(authors)):
                if search.lower() in authors[i].lower():
                    found.append(i)

            if not found:
                print("No results found!")
            else:
                print(f"\nFound {search}: ")
                print(f"{'Library Number':10}\t{'Title':<32}\t{'Author':30}\t{'Genre':30}\t{'Pages':5}\t{'Status':10}")
                print(f"\n--------------------------------------------------------------------------------------------------------------------------------------------")
                for i in range(0, len(found)):
                     print(f"{libraries[found[i]]:10}\t{titles[found[i]]:<32}\t{authors[found[i]]:30}\t{genres[found[i]]:30}\t{pages[found[i]]:5}\t{statuses[found[i]]:10}")
                
                print("--------------------------------------------------------------------------------------------------------------------------------------------\n")

    elif choice == "4":
            found = []
            search = input("Enter the Genre you are looking for: ")
            for i in range(0, len(genres)):
                if search.lower() in genres[i].lower():
                    found.append(i)

            if not found:
                print("No results found!")
            else:
                print(f"\nFound {search}: ")
                print(f"{'Library Number':10}\t{'Title':<32}\t{'Author':30}\t{'Genre':30}\t{'Pages':5}\t{'Status':10}")
                print(f"\n--------------------------------------------------------------------------------------------------------------------------------------------")
                for i in range(0, len(found)):
                     print(f"{libraries[found[i]]:10}\t{titles[found[i]]:<32}\t{authors[found[i]]:30}\t{genres[found[i]]:30}\t{pages[found[i]]:5}\t{statuses[found[i]]:10}")
                
                print("--------------------------------------------------------------------------------------------------------------------------------------------\n")
    elif choice == "5":
            search = input("Enter the Library Number you are looking for: ")

            min = 0
            max = len(titles) - 1
            mid = int((min + max) / 2 )

            while min < max and search.lower() != libraries[mid].lower():
                if search.lower() < libraries[mid].lower():
                    max = mid - 1
                else:
                    min = mid + 1

                mid = int((min + max) / 2 )
    
            if search.lower() == libraries[mid].lower():
                print(f"\nFound {search}: ")
                print(f"{'Library Number':10}\t{'Title':<32}\t{'Author':30}\t{'Genre':30}\t{'Pages':5}\t{'Status':10}")
                print(f"\n--------------------------------------------------------------------------------------------------------------------------------------------")
                print(f"{libraries[mid]:10}\t{titles[mid]:<32}\t{authors[mid]:30}\t{genres[mid]:30}\t{pages[mid]:5}\t{statuses[mid]:10}")
                print("--------------------------------------------------------------------------------------------------------------------------------------------\n")
            else:
                print("No results found!")

    elif choice == "6":
            found = []
            for i in range(0, len(statuses)):
                 if "available" in statuses[i].lower():
                      found.append(i)
            
            if not found:
                print("No results found!")
            else:
                print(f"\nCurrently Available Books:")
                print(f"{'Library Number':10}\t{'Title':<32}\t{'Author':30}\t{'Genre':30}\t{'Pages':5}\t{'Status':10}")
                print(f"\n--------------------------------------------------------------------------------------------------------------------------------------------")
                for i in range(0, len(found)):
                     print(f"{libraries[found[i]]:10}\t{titles[found[i]]:<32}\t{authors[found[i]]:30}\t{genres[found[i]]:30}\t{pages[found[i]]:5}\t{statuses[found[i]]:10}")
                
                print("--------------------------------------------------------------------------------------------------------------------------------------------\n")

    elif choice == "7":
            found = []
            for i in range(0, len(statuses)):
                 if "on loan" in statuses[i].lower():
                      found.append(i)
            
            if not found:
                print("No results found!")
            else:
                print(f"\nCurrently Loaned Books:")
                print(f"{'Library Number':10}\t{'Title':<32}\t{'Author':30}\t{'Genre':30}\t{'Pages':5}\t{'Status':10}")
                print(f"\n--------------------------------------------------------------------------------------------------------------------------------------------")
                for i in range(0, len(found)):
                     print(f"{libraries[found[i]]:10}\t{titles[found[i]]:<32}\t{authors[found[i]]:30}\t{genres[found[i]]:30}\t{pages[found[i]]:5}\t{statuses[found[i]]:10}")
                
                print("--------------------------------------------------------------------------------------------------------------------------------------------\n")
            
    elif choice == "8":
            print("Goodbye!")
            ans = "x"

    else:
            print("Invalid choice!")
