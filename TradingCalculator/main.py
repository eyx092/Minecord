from math import ceil

program_state = 1
#0: Not running
#1: Running

print("Tranding Calculator for Minecord")
print("Press Control-C to quit.")

def initialize():
    global emerald_value
    global lapis_value
    emerald_value = int(input("Set emerald value: "))
    lapis_value = int(input("Set lapis value: "))


def calculate_emerald_total():
    global amount
    global total
    global est_total
    global items_total
    amount = int(input("Input amount: "))
    total = amount * emerald_value
    est_total = ceil(round(total, -3))
    items_total = round(total / lapis_value)


def calculate_lapis_total():
    global amount
    global total
    global est_total
    global items_total
    amount = int(input("Input amount: "))
    total = amount * lapis_value
    est_total = ceil(round(total, -3))
    items_total = round(total / emerald_value)

def output(item):
    print("\n")
    print("Calculation")
    print("===================")
    if item == 1:
        print("Lapis amount:", (amount))
    if item == 2:
        print("Emerald amount:", (amount))
    print("Real Total:",(total))
    print("Rounded Total:",(est_total))
    if item == 1:
        print("Total in emeralds: ~",(items_total),sep="")
    if item == 2:
        print("Total in lapis: ~",(items_total),sep="")
    print("====================")
    print("Calculation end.")
    print("\n")

try:
    initialize()
    while program_state == 1:
        print("1. Calculate for emeralds")
        print("2. Calculate for lapis")
        option = input("Choose an option: ")
        if option == "1":
            calculate_emerald_total()
            output(2)
        elif option == "2":
            calculate_lapis_total()
            output(1)
        else:
            print("Not an option.")

except KeyboardInterrupt:
    program_state = 0
except ValueError:
    print("Not an integer.")
