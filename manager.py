import csv
from expense import Expense
from collections import deque
from datetime import datetime
from tabulate import tabulate


def save_in_csv (instance, filename='data/expenses.csv'):
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow( [ instance.date, instance.amount, instance.category, instance.description])




def instantiate_from_csv (class_name, filename='data/expenses.csv'):
    with open(filename, 'r', newline='') as f:
        reader = csv.DictReader(f)
        reader = list(reader)
        for expenses in reader:
            class_name(
                date=expenses.get('date'),
                amount=float(expenses.get('amount')),
                category=expenses.get('category'),
                description = expenses.get('description')
                )


def last_history(args : Expense, filename='data/expenses.csv') :
    N_rows = args.last
    with open(filename, 'r', newline='') as f:
        reader = csv.DictReader(f)
        reader = list(reader)
        last_history = deque(reader, maxlen=N_rows)
    # print(reader)
    # print ("date\t amount\t category\tdescription")
    # for item in last_history:
    #     print(f"{item.get('date')}\t{item.get('amount')}\t{item.get('category')}\t{item.get('description')}")
    # print(history)
    # print(f"{'Date':<12} {'Amount':>8} {'Category':<15} {'Description'}")
    # print("-" * 60)
    # for row in last_history:
    #     print(f"{row['date']:<12} {float(row['amount']):>8.2f} {row['category']:<15} {row['description']}")
        table = [
            [item['date'], float(item['amount']), item['category'], item['description']]
            for item in last_history
    ]
    headers = ["Date", "Amount", "Category", "Description"]

    print(tabulate(table, headers=headers, tablefmt="grid"))



def filter_by_date(args : Expense, filename='data/expenses.csv'):
    start_range = args.date_range_from
    end_range = args.to
    if not start_range or not end_range:
        print("Both --date_range_from and --to must be provided when filtering by date.")
        exit(1)
    with open(filename, 'r', newline='') as f:
        reader = csv.DictReader(f)
        filtered_rows = [
            row for row in reader
            if start_range <= datetime.strptime(row['date'], "%Y-%m-%d") <= end_range
            ]
        filtered_rows.sort(key=lambda row: datetime.strptime(row['date'], "%Y-%m-%d"))
        # print(f"{'Date':<12} {'Amount':>8} {'Category':<15} {'Description'}")
        # print("-" * 60)
        # for row in filtered_rows:
        #     print(f"{row['date']:<12} {float(row['amount']):>8.2f} {row['category']:<15} {row['description']}")
        table = [
        [item['date'], float(item['amount']), item['category'], item['description']]
        for item in filtered_rows
    ]

    headers = ["Date", "Amount", "Category", "Description"]

    print(tabulate(table, headers=headers, tablefmt="grid"))


def filter_by_category(args : Expense, filename='data/expenses.csv') : 
    with open(filename, 'r', newline='') as f:
        reader = csv.DictReader(f)
        filtered_rows = [
            row for row in reader
            if row.get('category') == args.category
            ]
        filtered_rows.sort(key=lambda row: datetime.strptime(row['date'], "%Y-%m-%d"))
    #         print(f"{'Date':<12} {'Amount':>8} {'Category':<15} {'Description'}")
    # print("-" * 60)
    # for row in filtered_rows:
    #     print(f"{row['date']:<12} {float(row['amount']):>8.2f} {row['category']:<15} {row['description']}")
        table = [
        [item['date'], float(item['amount']), item['category'], item['description']]
        for item in filtered_rows
    ]

    headers = ["Date", "Amount", "Category", "Description"]

    print(tabulate(table, headers=headers, tablefmt="grid"))


