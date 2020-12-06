from math import ceil

program_state = 1
#0: Not running
#1: Running

print("Trading Calculator for Minecord")
print("Press Control-C to quit.")

def initialize():
    global emerald_value
    global lapis_value
    global snow_value
    emerald_value = int(input("Set emerald value: "))
    lapis_value = int(input("Set lapis value: "))
    snow_value = int(input("Set snow value: "))


def calculate_emerald_total():
    global amount
    global total
    global est_total
    global lapis_total
    global snow_total
    amount = int(input("Input amount: "))
    total = amount * emerald_value
    est_total = ceil(round(total, -3))
    lapis_total = round(total / lapis_value)
    snow_total = round(total / snow_value)


def calculate_lapis_total():
    global amount
    global total
    global est_total
    global emeralds_total
    global snow_total
    amount = int(input("Input amount: "))
    total = amount * lapis_value
    est_total = ceil(round(total, -3))
    emeralds_total = round(total / emerald_value)
    snow_total = round(total / snow_value)

def calculate_snow_total():
    global amount
    global total
    global est_total
    global emeralds_total
    global lapis_total
    amount = int(input("Input amount: "))
    total = amount * snow_value
    est_total = ceil(round(total, -3))
    emeralds_total = round(total / emerald_value)
    lapis_total = round(total / lapis_value)

def output(item):
    print("\n")
    print("```")
    print("Calculation")
    print("===================")
    if item == 1:
        print("Lapis amount:", (amount))
    if item == 2:
        print("Emerald amount:", (amount))
    if item == 3:
        print("Snow amount:", (amount))
    print("Real Total:",(total))
    print("Rounded Total:",(est_total))
    if item == 1:
        print("Ballpark Total:", amount*35000)
    if item == 2:
        print("Ballpark Total:", amount*3000)
    if item == 1:
        print("Total in emeralds:", (emeralds_total))
        print("Total in snow:", (snow_total))
    if item == 2:
        print("Total in lapis:", (lapis_total))
        print("Total in snow:", (snow_total))
    if item == 3:
        print("Total in emeralds:", (emeralds_total))
        print("Total in lapis:", (lapis_total))
    print("====================")
    print("Calculation end.")
    print("```")
    print("\n")

try:
    initialize()
    while program_state == 1:
        print("1. Calculate for emeralds")
        print("2. Calculate for lapis")
        print("3. Calculate for snow")
        option = input("Choose an option: ")
        if option == "1":
            calculate_emerald_total()
            output(2)
        elif option == "2":
            calculate_lapis_total()
            output(1)
        elif option == "3":
            calculate_snow_total()
            output(3)
        else:
            print("Not an option.")

except KeyboardInterrupt:
    program_state = 0
except ValueError:
    print("Not an integer.")
