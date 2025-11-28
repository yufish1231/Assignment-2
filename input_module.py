# input_module.py
import csv
from datetime import datetime

CSV_FILE = "expenses.csv"

def add_expense():
    print("=== 支出輸入 ===")
    while True:
        date = input("日期 YYYY-MM-DD（留空=今天）： ").strip()
        if date == "":
            date = datetime.today().strftime("%Y-%m-%d")

        amt = input("金額（輸入 q 離開）： ").strip()
        if amt.lower() == "q":
            print("完成輸入。")
            break

        try:
            amt = float(amt)
        except:
            print("金額格式錯誤，請重新輸入。")
            continue

        cat = input("類別（Food, Transport...）： ").strip()
        if cat == "":
            cat = "Uncategorized"

        note = input("備註（可空）： ").strip()

        with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([date, amt, cat, note])
        
        print("✔ 已儲存\n")

if __name__ == "__main__":
    add_expense()
