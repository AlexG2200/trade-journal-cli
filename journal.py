#This is going to be a basic journal for be logging my trades ideas for sunday scans.
from flask import Flask,request, redirect, render_template
import datetime as dt

app = Flask(__name__)

""" def main_menu():
    print("welcome to the idea and stock journal")
    print("Enter 1 to journal ideas for the upcoming week")
    print("Enter 2 to journal aftermarket scan for the next day ")
    print("Enter 3 to quit and return to Main menu")
 """

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

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weekly", methods = ["POST"])
def weekly():
    Date = dt.date.today()
    Time = dt.datetime.now().strftime("%I:%M %p")

    Ticker = request.form["ticker"]
    Bias = request.form["bias"]
    Idea = request.form["idea"]

    entry_block = format_weekly_ideas(Date, Time, Ticker, Bias, Idea)
    append_to_file("Journal.txt", entry_block)

    return redirect("/")

@app.route("/aftermarket", methods = ["POST"])
def aftermarket():
    Date = dt.date.today()
    Time = dt.datetime.now().strftime("%I:%M %p")

    Ticker = request.form["ticker"]
    Catalyst = request.form["catalyste"]
    Levels = request.form["levels"]
    Plan = request.form["levels"]

    entry_block = format_aftermarket_scan(Date, Time, Ticker, Catalyst, Levels, Plan)
    append_to_file("afterday.txt", entry_block)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
