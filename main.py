import argparse
from expense import Expense
from utils import validate_date
from utils import positive_amount
from manager import save_in_csv
from manager import last_history
from manager import filter_by_date
from manager import filter_by_category
from report import summary_maker
from visualize import chart_maker


#CLI 
def parser():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--date", type=validate_date, required=True, help="Expense date")
    add_parser.add_argument("--amount", type=positive_amount, required=True, help="Expense amount")
    add_parser.add_argument("--category", type=str, required=True, help="Expense category")
    add_parser.add_argument("--description", type=str, required=False, help="Expense discription")
    summary_parser = subparsers.add_parser("summary", help="Generate expense summary")

    visualize_parser = subparsers.add_parser("visualize", help="visualizes expenses")
#history
    history_parser = subparsers.add_parser("history", help="Show expense history")
    history_parser.add_argument("--last", type=int, default=10)
    #history filtering
    history_parser.add_argument("--filtered_by", type=str, required=False, help="Filter type")
    #history filters by date
    history_parser.add_argument("--date_range_from", type=validate_date, required=False, help="start range")
    history_parser.add_argument("--to", type=validate_date, required=False, help="end range")
    #history filters by category
    history_parser.add_argument("--category", type=str, required=False, help="enter category name")

    args = parser.parse_args()
    return args


def handle_add(args):
    try:
        new_expense = Expense(
            amount=args.amount,
            date=args.date,
            category=args.category,
            description=args.description or ""
        )

        save_in_csv(new_expense)
        print("✅ Expense added successfully.")

    except Exception as e:
        print(f"❌ Error adding expense: {e}")

def handle_history(args):
    try:
        if not args.filtered_by:
            last_history(args.last)

        elif args.filtered_by == "date":
            filter_by_date(args.date_range_from, args.to)

        elif args.filtered_by == "category":
            filter_by_category(args.category)

        else:
            print("⚠️ Unsupported filter type.")

    except Exception as e:
        print(f"❌ Error displaying history: {e}")

def handle_summary(args):
    try:
        summary_maker()  
    except Exception as e:
        print(f"❌ Error generating summary: {e}")


def handle_visualize():
    try:
        chart_maker()  
    except Exception as e:
        print(f"❌ Error generating summary: {e}")


#command analys
def command_analyser(args) :
    if args.command == "add" :
        handle_add(args)
        print(args.date)
        
    elif args.command == "history" :
        handle_history(args)
            

    elif args.command == "summary":
        handle_summary(args)

    elif args.command == "visualize":
        handle_visualize()


    else :
        raise "invailable argument"

def main():
    args = parser()
    command_analyser(args)


if __name__ == "__main__":
    main()