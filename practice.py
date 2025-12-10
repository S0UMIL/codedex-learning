def currency_converter(from_currency):
    rates = {
    'usd': 0.012,
    'euro': 0.011,
    'yen': 1.75,
    'inr': 1
}
    def convert(amount, to_currency):
        if from_currency not in rates or to_currency not in rates:
            return "unavailable"
        else:
            amount_in_inr = amount * rates[from_currency]
            return amount_in_inr * rates[from_currency]
    return convert
       
    


            