class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination.name}")
            destination.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, '*') + '\n'
        items = ''
        for entry in self.ledger:
            description = entry.get('description', '')[:23].ljust(23)
            amount = f"{entry.get('amount', 0):.2f}"[:7].rjust(7)
            items += f"{description}{amount}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    spent = []
    names = [cat.name for cat in categories]
    for cat in categories:
        s = sum(item["amount"] for item in cat.ledger if item["amount"] < 0)
        spent.append(abs(s))
    
    total = sum(spent)
    percentages = [int((s / total * 100) // 10) * 10 for s in spent] if total > 0 else [0 for _ in spent]

    chart = "Percentage spent by category"

    for i in range(100, -1, -10):
        chart += "\n" + str(i).rjust(3) + "| "
        for p in percentages:
            chart += "o  " if p >= i else "   "

    chart += "\n    " + "-" * (len(categories) * 3 + 1)

    max_len = max(len(name) for name in names)
    for i in range(max_len):
        chart += "\n     "
        for name in names:
            chart += (name[i] if i < len(name) else " ") + "  "
        
    return chart
