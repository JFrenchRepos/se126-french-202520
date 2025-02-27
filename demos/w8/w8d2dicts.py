#w8d2 - intro to dictionaries 2

#dictionaries are collections similar to arrays in javascript

#--IMPORTS--
import csv
#--CODE--
library = {
    "1230": "Red Rising",
    "1231": "Le Petit Prince"

}

#--connected--
with open("textfiles/w8/dictionary_file.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        library.update({rec[0]: rec[1]})
#--disconnected--

print(f"{'KEY':4}: {'TITLE'}")
print("-" * 50)
for key in library:
    print(f"{key.upper():4}: {library[key]}")
print("-" * 50)

#--sequential search--
search = input("\nEnter the Title you are looking for: ")

found = 0

for key in library:
    if search.lower() == library[key].lower():
        found = key

if found != 0:
    print(f"Found {search.upper()}:")
    print("-" * 50)
    print(f"{found.upper():4}: {library[found]}")
    print("-" * 50)
else:
    print(f"{search.upper()} not found")
