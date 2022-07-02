import datetime
def parse_expenses(expenses_string):
    expenses = []
    for line in expenses_string.splitlines():
        if line.startswith("#"):
            continue
        date, value, currency = line.split(" ")
        expenses.append((datetime.datetime.strptime(date, "%Y-%m-%d"),
                        float(value),
                        currency))
    return expenses

expenses_string = "2016-01-02 -34.01 USD"

print(parse_expenses(expenses_string))
