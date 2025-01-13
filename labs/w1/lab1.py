#Joshua French
#SE126.04
#LAB 1
#1-12-2025

#PROGRAM PROMPT: This is a program that determines whether a meeting room is in violation of fire regulations regarding the maximum room capacity.

#VARIABLE DICTIONARY
#name           meeting name
#people         number of people
#maxpeople      maximum of allowed people in room
#diff           maxpeople compared to people
#res            loop controller for checking if user requires more inputs

#-------------------------------------------------------------------------------------------------------------------------------------------------#
#FUNCTIONS
#-------------------------------------------------------------------------------------------------------------------------------------------------#
def difference(people, maxpeople):
    diff = maxpeople - people
    return diff

def response(res):
    while res != "y" and res != "n":
            print("###Invalid answer, resubmit###")
            print("")
            res = input("Check a room? (Y/N): ").lower()

    if res == "y":
        return res
    else:
        print("----------=====GOODBYE!=====----------")
#-------------------------------------------------------------------------------------------------------------------------------------------------#
#CODE START
#-------------------------------------------------------------------------------------------------------------------------------------------------#
print("----------=====FIRE REGULATION CHECKER=====----------")
res = input("Start? (Y/N): ").lower()
print("")
while res != "y" and res != "n":
    print("###Invalid answer, resubmit###")
    print("")
    res = input("Start? (Y/N): ").lower()

while res == "y":
    response(res)      
    print("----------=====CAPACITY=====----------")
    name = str(input("What is the meeting name?: "))
    print("")

    people = int(input("How many people will be attending?: "))
    print("")

    maxpeople = int(input("What is the meeting room's maximum allowed capacity?: "))
    print("")

    diff = difference(people, maxpeople)
    if diff > 0:
        print("||", name, "can fit", abs(diff),"more people, and it meets fire regulations. ||")
        print("")
    if diff < 0:
        print("|#|", name, "is over capacity! Remove", abs(diff),"people to meet with fire regulations! |#|")
        print("")
    elif diff == 0:
        print("||", name, "has reached capacity. ||")
    print("")

    res = input("Start again? (Y/N): ").lower()
    while res != "y" and res != "n":
        print("###Invalid answer, resubmit###")
        print("")
        res = input("Start? (Y/N): ").lower()

print("----------=====GOODBYE!=====----------")
