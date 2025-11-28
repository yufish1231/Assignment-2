# visualization_module.py
import csv
import os
import time
import matplotlib.pyplot as plt

CSV_FILE = "expenses.csv"

def load_and_plot():
    while True:
        if not os.path.exists(CSV_FILE):
            print("目前還沒有資料，等待中...")
            time.sleep(3)
            continue
        
        totals = {}
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            for row in csv.reader(f):
                if len(row) < 3:
                    continue
                amount = float(row[1])
                category = row[2]
                totals[category] = totals.get(category, 0) + amount

        plt.clf()
        if totals:
            plt.pie(totals.values(), labels=totals.keys(), autopct="%1.1f%%")
            plt.title("Expenses by Category")
        else:
            plt.text(0.5, 0.5, "No data", ha="center", va="center")

        plt.pause(1)
        time.sleep(2)

if __name__ == "__main__":
    plt.ion()
    load_and_plot()
