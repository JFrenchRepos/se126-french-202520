# Joshua French
# SE126.04
# LAB 7
# 3-1-2025

# PROGRAM PROMPT: Build a mini programming dictionary a user can search through and ad to using the words.csv file.

#--IMPORTS--
import csv

def menu():
    print("\nDictionary Menu")
    print("1. Show all words")
    print("2. Search for a word")
    print("3. Add a word")
    print("3.5 Show all words alphabetically")
    print("4. EXIT")
    return input("Enter your choice: ").strip()

#--CODE--
updatedfile = "updatedwords.csv"
dictionary = {}
with open("textfiles/w9/words.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        word, definition = rec
        dictionary[word.lower()] = definition

loop = "x"
while loop == "x":
    choice = menu()

    if choice == "1":
        if dictionary:
            for word, definition in dictionary.items():
                print(f"{word}: {definition}")
        else:
                print("The dictionary is empty.")

    elif choice == "2":
        word = input("Enter the word to search: ").strip().lower()
        if word in dictionary:
            print(f"{word}: {dictionary[word]}")
        else:
            print(f"{word} is not in the dictionary.")

    elif choice == "3":
        word = input("Enter the word to add: ").strip().lower()
        if word in dictionary:
            print(f"{word} already exists in the dictionary.")
        else:
            definition = input("Enter the definition: ").strip()
            dictionary[word] = definition
            print(f"{word} has been added to the dictionary.")

    elif choice == "3.5":
        if dictionary:
            for word in sorted(dictionary.keys()):
                print(f"{word}: {dictionary[word]}")
        else:
                print("The dictionary is empty.")

    elif choice == "4":
            loop = "n"
            with open(updatedfile, mode='w', newline='') as newfile:
                writer = csv.writer(newfile)
                for word, definition in dictionary.items():
                    writer.writerow([word, definition])
            print(f"Dictionary saved to {updatedfile}.")

    else:
        print("Invalid choice. Please try again.")
