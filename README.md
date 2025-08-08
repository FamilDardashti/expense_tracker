# Expense Tracker

Expense Tracker is a lightweight command‑line application for recording daily spending in a CSV file and generating useful summaries and charts. It is ideal for quickly tracking expenses without relying on a full database or web interface.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Adding an expense](#adding-an-expense)
  - [Viewing history](#viewing-history)
  - [Summary](#summary)
  - [Visualization](#visualization)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Add expense entries with a date, amount, category, and optional description.
- Show the most recent entries or filter history by date range or category.
- Produce a summary that reports totals by category and the average daily spending. The output is saved to `reports/summary.txt`.
- Visualize expenses with bar and line charts saved in the `reports` directory.

## Getting Started

### Prerequisites

- Python 3.10+
- Python packages: `pandas`, `matplotlib`, and `tabulate`

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd expense_tracker
   ```

2. (Optional) Create and activate a virtual environment.

3. Install the dependencies:

   ```bash
   pip install pandas matplotlib tabulate
   ```

4. Create folders for data storage and generated reports:

   ```bash
   mkdir -p data reports
   ```

## Usage

Run the CLI by invoking `main.py` with one of the available commands.

```bash
python main.py <command> [--argument value]
```

### Adding an expense

```bash
python main.py add --date 2025-07-01 --amount 120 --category food --description "grocery shopping"
```

### Viewing history

```bash
python main.py history
python main.py history --last 5
python main.py history --filtered_by date --date_range_from 2025-07-01 --to 2025-07-15
python main.py history --filtered_by category --category food
```

### Summary

```bash
python main.py summary
```

### Visualization

```bash
python main.py visualize
```

The visualization command produces a bar chart of spending by category and a line chart of daily totals. Both images are saved under `reports/`.

## Project Structure

```
├── expense.py      # Expense data model
├── main.py         # Command-line interface
├── manager.py      # CSV storage and history filtering
├── report.py       # Summary generation
├── utils.py        # Input validators
└── visualize.py    # Chart rendering
```

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to open a pull request or submit an issue on GitHub.

## License

This project is provided without a specific license. Use at your own discretion.
