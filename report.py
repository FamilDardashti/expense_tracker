import pandas as pd
from tabulate import tabulate


def write_tabulated_summary_to_file(total, filter, average, filename="reports/summary.txt"):
    table = tabulate(filter, headers="keys", tablefmt="grid")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Total Expenses : {total}")
        f.write("\n\nBy category :\n")
        f.write(table)
        f.write(f"\n\nDaily average : {average}")



def summary_maker(filename='data/expenses.csv') :
    df = pd.read_csv(filename)
    total = df.groupby("category")["amount"].sum().sum()
    filter = df.groupby("category")["amount"].sum().reset_index()
    average = df.groupby("date")["amount"].mean().mean()
    print(f"Total Expenses : {total}")
    print("\nBy category :")
    print(tabulate(filter, headers='keys', tablefmt='grid'))
    print(f"\nDaily average : {average}")
    write_tabulated_summary_to_file(total, filter, average)

