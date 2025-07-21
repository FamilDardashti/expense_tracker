import re
from datetime import datetime
import argparse


#date format validation


def validate_date(date_str):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_str):
        raise argparse.ArgumentTypeError("❌ Date must be in YYYY-MM-DD format")
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise argparse.ArgumentTypeError("❌ Invalid date (like 2025-13-40)")


#amount validation
def positive_amount(value):
    try:
        f = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError("Amount must be a number")
    if f < 0:
        raise argparse.ArgumentTypeError("Amount must be non-negative")
    return f
