
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

def chart_maker():
    try:
        df = pd.read_csv("data/expenses.csv")
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
        category_sum = df.groupby("category")["amount"].sum()
        category_sum.plot(kind="bar", color='#5f4b8b')
        
        
        date_sum = df.groupby("date")["amount"].sum().sort_index()
        plt.xlabel("Category")
        plt.ylabel("Total Amount")
        plt.title("Total Expenses by Category")
        plt.tight_layout()
        plt.savefig("category_spending_bar.png", dpi=300, bbox_inches="tight")
        plt.show()
        
        
        date_sum.plot(kind="line",marker = 'o',c = '#ff6f61',mfc= '#ff4433',mec= '#ff4433')
        plt.xlabel("date")
        plt.ylabel("Total Amount")
        plt.title("Daily Total Expenses")
        plt.tight_layout()
        plt.savefig("reports/daily_expense_line.png", dpi=300, bbox_inches="tight")
        plt.show()

    except Exception as e:
        print(f"❌ Error generating summary: {e}")
    else:    
        print("✅ Charts have been saved successfully in the 'reports' folder!")
