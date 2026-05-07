import csv
import os
from datetime import datetime, date
import matplotlib.pyplot as plt


# =============================
# -------- HELPERS ------------
# =============================

def safe_input(prompt: str) -> str:
    return input(prompt).strip()


def parse_amount(value: str) -> float:
    try:
        amount = float(value)
    except ValueError:
        raise ValueError("Amount must be numeric (example: 12.50).")

    if amount <= 0:
        raise ValueError("Amount must be greater than 0.")
    return amount


def clean_category(cat: str) -> str:
    cat = cat.strip()
    if not cat:
        raise ValueError("Category cannot be empty.")
    return cat.title()


def clean_type(t: str) -> str:
    t = t.lower().strip()
    if t in ("income", "i"):
        return "income"
    if t in ("expense", "e"):
        return "expense"
    raise ValueError("Type must be 'income' or 'expense'.")


def current_month():
    today = date.today()
    return f"{today.year:04d}-{today.month:02d}"


# =============================
# -------- QUICK ADD ----------
# =============================

def parse_quick_add(line: str):
    parts = line.split()
    if len(parts) < 2:
        raise ValueError("Example: expense food 7.50 coffee")

    first = parts[0].lower()

    # If first word is type
    if first in ("income", "expense", "i", "e"):
        tx_type = clean_type(parts[0])
        rest = parts[1:]

        if len(rest) < 2:
            raise ValueError("After type include: category amount")

        # Try category amount
        try:
            category = clean_category(rest[0])
            amount = parse_amount(rest[1])
            note = " ".join(rest[2:])
            return tx_type, category, amount, note
        except:
            pass

        # Try amount category
        try:
            amount = parse_amount(rest[0])
            category = clean_category(rest[1])
            note = " ".join(rest[2:])
            return tx_type, category, amount, note
        except:
            raise ValueError("Could not parse. Example: expense food 7.50 coffee")

    # Backward compatibility → default expense
    tx_type = "expense"

    try:
        category = clean_category(parts[0])
        amount = parse_amount(parts[1])
        note = " ".join(parts[2:])
        return tx_type, category, amount, note
    except:
        pass

    try:
        amount = parse_amount(parts[0])
        category = clean_category(parts[1])
        note = " ".join(parts[2:])
        return tx_type, category, amount, note
    except:
        raise ValueError("Could not parse input.")


def quick_add(transactions):
    print("\nQuick Add (date = today)")
    print("Example:")
    print("  expense food 7.50 coffee")
    print("  income salary 1500 paycheck")

    while True:
        line = safe_input("Enter transaction: ")
        try:
            tx_type, category, amount, note = parse_quick_add(line)
            break
        except ValueError as e:
            print("❌", e)

    transactions.append({
        "date": date.today(),
        "type": tx_type,
        "amount": amount,
        "category": category,
        "note": note
    })

    symbol = "➕" if tx_type == "income" else "➖"
    print(f"✅ Added: {symbol} €{amount:.2f} | {tx_type.upper()} | {category}")


# =============================
# -------- FILE IO ------------
# =============================

def load_transactions(filename):
    transactions = []

    if not os.path.exists(filename):
        return transactions

    with open(filename, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                transactions.append({
                    "date": datetime.strptime(row["date"], "%Y-%m-%d").date(),
                    "type": row["type"],
                    "amount": float(row["amount"]),
                    "category": row["category"],
                    "note": row.get("note", "")
                })
            except:
                continue

    return transactions


def save_transactions(filename, transactions):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "type", "amount", "category", "note"])
        writer.writeheader()
        for t in transactions:
            writer.writerow({
                "date": t["date"].isoformat(),
                "type": t["type"],
                "amount": f"{t['amount']:.2f}",
                "category": t["category"],
                "note": t["note"]
            })


# =============================
# -------- SUMMARY ------------
# =============================

def filter_month(transactions, month):
    if not month:
        return transactions

    try:
        dt = datetime.strptime(month, "%Y-%m")
    except:
        print("⚠️ Invalid month format. Showing all time.")
        return transactions

    return [t for t in transactions if t["date"].year == dt.year and t["date"].month == dt.month]


def summary(transactions, month=None):
    data = filter_month(transactions, month)

    income = sum(t["amount"] for t in data if t["type"] == "income")
    expense = sum(t["amount"] for t in data if t["type"] == "expense")
    balance = income - expense

    print("\n📊 SUMMARY")
    print(f"Income:   €{income:.2f}")
    print(f"Expenses: €{expense:.2f}")
    print(f"Balance:  €{balance:.2f}")


# =============================
# -------- MAIN ---------------
# =============================

def main():
    filename = "transactions.csv"
    transactions = load_transactions(filename)

    print("\nPersonal Finance Tracker")
    print("----------------------------------")
    first_choice = safe_input("Press Enter for Quick Add, or type menu number: ")

    if first_choice == "":
        quick_add(transactions)
        summary(transactions, current_month())

    while True:
        print("\nMENU")
        print("1) Quick add")
        print("2) Show summary")
        print("3) Save & Exit")

        choice = safe_input("Choose option: ")

        if choice == "1":
            quick_add(transactions)

        elif choice == "2":
            month = safe_input("Month (YYYY-MM) or Enter for all: ")
            month = month if month else None
            summary(transactions, month)

        elif choice == "3":
            save_transactions(filename, transactions)
            print("✅ Saved. Goodbye!")
            break

        else:
            print("❌ Invalid option.")


if __name__ == "__main__":
    main()