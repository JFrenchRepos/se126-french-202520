import csv 

total_rec = 0 

print(f"{'FIRST':10}  {'LAST':10}  {'NUM':3}  {'CLASS1':7}  {'CLASS2'}")
print("-----------------------------------------------------------")
with open("demos/w2/csvs/unevenRecords.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        total_rec += 1

        first = rec[0]
        last = rec[1]
        num = int(rec[2]) #***** KEY
        class1 = rec[3]

        #IF num is 1, there is only 1 class listed (rec[3])
        #IF NUM is 2, there are two classes listed (rec[3], rec[4])

        if num == 2:
            class2 = rec[4]
        else:
            class2 = "-----"

        print(f"{first:10}  {last:10}  {num:1}    {class1:7}  {class2}")
print("-----------------------------------------------------------")
print(f"\nThere are {total_rec} students in the file.\n\n")