import argparse
import csv
from expense import expense
from utils import validate_date
from utils import positive_amount
from manager import save_in_csv
from manager import instantiate_from_csv
from manager import last_history
from manager import filter_by_date
from manager import filter_by_category
from manager import summary_maker

#CLI 
def parser():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--date", type=str, required=True, help="Expense date")
    add_parser.add_argument("--amount", type=positive_amount, required=True, help="Expense amount")
    add_parser.add_argument("--category", type=str, required=True, help="Expense category")
    add_parser.add_argument("--description", type=str, required=False, help="Expense discription")

    summary_parser = subparsers.add_parser("summary", help="Generate expense summary")
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

def obj_maker (args):
    new_expense = expense(date = args.date,
                         amount = args.amount,
                         category = args.category,
                         description = args.description
                         )
    save_in_csv(new_expense)

#command analys
def command_analyser(args) :
    if args.command == "add" :
        assert validate_date(args.date) , "❌ Error: Enter date in YYYY-MM-DD format"
        obj_maker(args)
        
    elif args.command == "history" :
        if not args.filtered_by:
            last_history(args)
        
        elif args.filtered_by == "date" :
            filter_by_date(args)

        elif args.filtered_by == "category" :
            filter_by_category(args)

        else : 
            print("chose date or category filtering")
            exit(1) 
            


    elif args.command == "summary":
        summary_maker()


    else :
        raise "invailable argument"


args = parser()
command_analyser(args)