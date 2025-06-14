import database
import analyze

def menu():
    print("\n---- Expense Tracker ----")
    print("1. Add Expense")
    print("2. Show Daily Totals")
    print("3. Show Category Summary")
    print("4. Show Monthly Summary")
    print("5. Exit")

while True:
    menu()
    choice = input("Choose option: ")

    if choice == "1":
        try:
            amount = float(input("Amount: "))
            category = input("Category (e.g., food, rent, travel): ")
            database.add_expense(amount, category)
            print("Expense added.")
        except Exception as e:
            print("Error:", e)

    elif choice == "2":
        for date, total in analyze.daily_total():
            print(f"{date} - ${total:.2f}")

    elif choice == "3":
        for cat, total in analyze.category_summary():
            print(f"{cat} - ${total:.2f}")

    elif choice == "4":
        for month, total in analyze.monthly_summary():
            print(f"{month} - ${total:.2f}")

    elif choice == "5":
        break

    else:
        print("Invalid option.")
