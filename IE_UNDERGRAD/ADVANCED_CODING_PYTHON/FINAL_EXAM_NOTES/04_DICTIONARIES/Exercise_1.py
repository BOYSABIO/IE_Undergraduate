currencies = {
    "Euro":"e",
    "Dollar":"$",
    "Yen":"t"
}

currency = input("Please enter a currency: ")
print(currencies.get(currency.title(), "Currency is missing.")) # Converts string to a title input

