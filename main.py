from time import strftime #for timestamps

stored_prices = []
stored_price_paid = []
stored_items_given = []
time_stamps = []
print("Minecord Tracking Tool v1.0")
print("Press Control-C to exit.")

def find_average():
    try:
        sum = 0
        stored_prices_length = len(stored_prices)
        for i in range(stored_prices_length):
            sum += stored_prices[i]
        session_average = sum / stored_prices_length
        print(session_average)
    except ZeroDivisionError:
        print("Div0 Error")
        print("No data")

while True:
    try:
        print("0. Add trade")
        print("1. Access memory")
        print("2. Compute average")
        print("3. Access memory by trade")
        selection = input(">")

        if selection == "0":
            price_paid = int(input("Price paid: "))
            items_given = int(input("Items given: "))
            stored_price_paid.append(price_paid)
            stored_items_given.append(items_given)
            unit_price = price_paid / items_given
            stored_prices.append(unit_price)
            time_stamps.append(strftime("%H:%M:%S")+" EST")

        if selection == "1":
            print("Stored Prices:",stored_prices)
            print("Time Stamps:",time_stamps)

        if selection == "2":
            find_average()

        if selection == "3":
            stored_prices_length = len(stored_prices)
            if stored_prices_length == 0:
                print("No trades in memory.")
            for i in range(stored_prices_length):
                print("Trade", (i))
                print("Unit Price:", (stored_prices[i]))
                print("Price Paid:", (stored_price_paid[i]))
                print("Items Given:", (stored_items_given[i]))
                print("Time Recorded:", (time_stamps[i]))
                print("\n")

    except KeyboardInterrupt:
        print()
        print("Final Unit Prices:", stored_prices)
        print("Final Time Stamps:",time_stamps)
        print("Final Average:")
        find_average()
        break

    except:
        print()


