from forex_python.converter import CurrencyRates

def get_currency(x):
    c = CurrencyRates()
    a,b=x.split()
    return c.get_rate(a,b)