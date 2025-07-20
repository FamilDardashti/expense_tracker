class Expense:
    all = []
       
    def __init__ (self, amount : float, date, category: str, description = ""):
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description
        Expense.all.append(self)
        
    def __repr__ (self):
        return f"expense ({self.amount}$ at {self.date} in {self.category} category for {self.description})"
