#This is going to be a basic journal for be logging my trades ideas for sunday scans.

import datetime as dt


def main_menu():
    print("welcome to the idea and stock journal")
    print("Enter 1 to journal ideas for the upcoming week")
    print("Enter 2 to journal aftermarket scan for the next day ")
    print("Enter 3 to quit and return to Main menu")

def append_to_file(filename,text):
    file = open(filename, "a")
    file.write(text)
    file.close()
    

def format_weekly_ideas(Date,Time,Ticker,Bias,Idea):
    return (
        "============================\n"
        f"WEEKLY IDEA | Date: {Date} Time: {Time}\n"
        f"Ticker: {Ticker}\n"
        f"Bias: {Bias}\n"
        "Idea: \n"
        f"   {Idea}\n"
        "============================\n\n"
    )

#continu here with the format_aftermarket scan
def format_aftermarket_scan(Date, Time, Ticker, Catalyst, Levels, Plan):
    return (
        "============================\n"
        f"AFTERMARKET SCAN | Date: {Date} Time: {Time}\n"
        f"Ticker: {Ticker}\n"
        f"Catalyst: {Catalyst}\n"
        f"Levels: {Levels}\n"
        "Plan:\n"
        f"  {Plan}\n"
        "============================\n\n"
    )


def weekly_trade_ideas():
    
    add_more  = "y"
    while add_more == "y":
    #gets the current date and time
        Date = dt.date.today()
        Time = dt.datetime.now().strftime("%I:%M %p")
    # asks for important info
        Ticker = input("Enter Ticker: ")
        Bias = input("Enter bias (bullish / bearish / neutral): ")
        Idea = input("Describe your trade idea: ")

        entry_block = format_weekly_ideas(
            Date,
            Time,
            Ticker,
            Bias,
            Idea
        )

        append_to_file("journal.txt", entry_block)
        add_more = input("Add another trade idea? y/n")

        if add_more == "n":
            return

def aftermarket_scan():
    add_more = "y"
    while add_more == "y":
        #gets the current date and time
        Date = dt.date.today()
        Time = dt.datetime.now().strftime("%I:%M %p")

        Ticker = input("Enter Ticker: ")
        Catalyst = input("Enter catalyst (news / earnings / none): ")
        Levels = input("Enter key levels: ")
        Plan = input("Plan for tomorrow: ")

        entry_block = format_aftermarket_scan(
            Date,
            Time,
            Ticker,
            Catalyst,
            Levels,
            Plan
        )

    # appending to the file
        append_to_file("journal.txt", entry_block)
        add_more = input("Add another trade idea? y/n")

        if add_more == "n":
            return

        

def main():

    while True:
        main_menu()
        choice_str = input("Please choose from one of the following options ").strip()
        if not choice_str.isdigit():
            print("Please enter a number (1-3).")
            continue
        choice = int(choice_str)

        if choice == 1:
            weekly_trade_ideas()

        elif choice == 2:
            aftermarket_scan()

        elif choice == 3:
            print("Exiting program")
            return
        else:
            print("Invalid Choice. Try again ")

        

if __name__ == "__main__":
    main()



