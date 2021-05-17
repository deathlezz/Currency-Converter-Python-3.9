# Currency Converter
# Python 3.9.1
# Created by deathlezz
# Date 17.05.2021


from pip._vendor import requests


class CurrencyConverter:

    def __init__(self, url):

        try:
            self.data = requests.get(url).json()
            self.currencies = self.data['rates']

        # Avoid internet connection error
        except requests.exceptions.ConnectionError:
            print()
            print('* No internet connection *')
            exit()


    def convert(self, from_currency, to_currency, amount):

        # Convert currency to USD if it is not USD because our base currency is USD.
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]

        # Rounding to 6 decimal places and avoiding scientific notation
        amount = ("%.6f" % (amount * self.currencies[to_currency])).rstrip('0').rstrip('.')
        return amount

        # Use this to round only:
        # amount = round(amount * self.currencies[to_currency], 4)

# Currencies rate API
url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = CurrencyConverter(url)


# Main program start here
print()
print('* Welcome to Currency Converter *')

# Infinite loop
while True:

    print()
    print('Choose currency to convert:')
    print('[1] USD / [2] EUR / [3] JPY / [4] GBP / [5] AUD / [6] CAD / [7] CHF')
    print()

    try:
        userChoice = int(input('Enter your choice: '))
        print()
    except ValueError:
        print()
        print('* Enter numbers only *')
        continue

    if userChoice == 1:     # USD

        try:
            value = float(input('Enter value to convert: '))
            print()
        except ValueError:
            print()
            print('* Enter numbers only *')
            continue

        if value > 0:

            usdEur = converter.convert('USD', 'EUR', value)
            usdJpy = converter.convert('USD', 'JPY', value)
            usdGbp = converter.convert('USD', 'GBP', value)
            usdAud = converter.convert('USD', 'AUD', value)
            usdCad = converter.convert('USD', 'CAD', value)
            usdChf = converter.convert('USD', 'CHF', value)

            print(f'{value} $ = {usdEur} €')
            print(f'{value} $ = {usdJpy} ¥')
            print(f'{value} $ = {usdGbp} £')
            print(f'{value} $ = {usdAud} AU$')
            print(f'{value} $ = {usdCad} CA$')
            print(f'{value} $ = {usdChf} Fr')

        else:
            print('* Enter value bigger than 0 *')

    elif userChoice == 2:     # EUR

        try:
            value = float(input('Enter value to convert: '))
            print()
        except ValueError:
            print()
            print('* Enter numbers only *')
            continue

        if value > 0:

            eurUsd = converter.convert('EUR', 'USD', value)
            eurJpy = converter.convert('EUR', 'JPY', value)
            eurGbp = converter.convert('EUR', 'GBP', value)
            eurAud = converter.convert('EUR', 'AUD', value)
            eurCad = converter.convert('EUR', 'CAD', value)
            eurChf = converter.convert('EUR', 'CHF', value)

            print(f'{value} € = {eurUsd} $')
            print(f'{value} € = {eurJpy} ¥')
            print(f'{value} € = {eurGbp} £')
            print(f'{value} € = {eurAud} AU$')
            print(f'{value} € = {eurCad} CA$')
            print(f'{value} € = {eurChf} Fr')

        else:
            print('* Enter value bigger than 0 *')

    elif userChoice == 3:     # JPY

        try:
            value = float(input('Enter value to convert: '))
            print()
        except ValueError:
            print()
            print('* Enter numbers only *')
            continue

        if value > 0:

            jpyUsd = converter.convert('JPY', 'USD', value)
            jpyEur = converter.convert('JPY', 'EUR', value)
            jpyGbp = converter.convert('JPY', 'GBP', value)
            jpyAud = converter.convert('JPY', 'AUD', value)
            jpyCad = converter.convert('JPY', 'CAD', value)
            jpyChf = converter.convert('JPY', 'CHF', value)

            print(f'{value} ¥ = {jpyUsd} $')
            print(f'{value} ¥ = {jpyEur} €')
            print(f'{value} ¥ = {jpyGbp} £')
            print(f'{value} ¥ = {jpyAud} AU$')
            print(f'{value} ¥ = {jpyCad} CA$')
            print(f'{value} ¥ = {jpyChf} Fr')

        else:
            print('* Enter value bigger than 0 *')

    elif userChoice == 4:     # GBP

        try:
            value = float(input('Enter value to convert: '))
            print()
        except ValueError:
            print()
            print('* Enter numbers only *')
            continue

        if value > 0:

            gbpUsd = converter.convert('GBP', 'USD', value)
            gbpEur = converter.convert('GBP', 'EUR', value)
            gbpJpy = converter.convert('GBP', 'JPY', value)
            gbpAud = converter.convert('GBP', 'AUD', value)
            gbpCad = converter.convert('GBP', 'CAD', value)
            gbpChf = converter.convert('GBP', 'CHF', value)

            print(f'{value} £ = {gbpUsd} $')
            print(f'{value} £ = {gbpEur} €')
            print(f'{value} £ = {gbpJpy} ¥')
            print(f'{value} £ = {gbpAud} AU$')
            print(f'{value} £ = {gbpCad} CA$')
            print(f'{value} £ = {gbpChf} Fr')

        else:
            print('* Enter value bigger than 0 *')

    elif userChoice == 5:     # AUD

        try:
            value = float(input('Enter value to convert: '))
            print()
        except ValueError:
            print()
            print('* Enter numbers only *')
            continue

        if value > 0:

            audUsd = converter.convert('AUD', 'USD', value)
            audEur = converter.convert('AUD', 'EUR', value)
            audJpy = converter.convert('AUD', 'JPY', value)
            audGbp = converter.convert('AUD', 'GBP', value)
            audCad = converter.convert('AUD', 'CAD', value)
            audChf = converter.convert('AUD', 'CHF', value)

            print(f'{value} AU$ = {audUsd} $')
            print(f'{value} AU$ = {audEur} €')
            print(f'{value} AU$ = {audJpy} ¥')
            print(f'{value} AU$ = {audGbp} £')
            print(f'{value} AU$ = {audCad} CA$')
            print(f'{value} AU$ = {audChf} Fr')

        else:
            print('* Enter value bigger than 0 *')

    elif userChoice == 6:     # CAD

        try:
            value = float(input('Enter value to convert: '))
            print()
        except ValueError:
            print()
            print('* Enter numbers only *')
            continue

        if value > 0:

            cadUsd = converter.convert('CAD', 'USD', value)
            cadEur = converter.convert('CAD', 'EUR', value)
            cadJpy = converter.convert('CAD', 'JPY', value)
            cadGbp = converter.convert('CAD', 'GBP', value)
            cadAud = converter.convert('CAD', 'AUD', value)
            cadChf = converter.convert('CAD', 'CHF', value)

            print(f'{value} CA$ = {cadUsd} $')
            print(f'{value} CA$ = {cadEur} €')
            print(f'{value} CA$ = {cadJpy} ¥')
            print(f'{value} CA$ = {cadGbp} £')
            print(f'{value} CA$ = {cadAud} AU$')
            print(f'{value} CA$ = {cadChf} Fr')

        else:
            print('* Enter value bigger than 0 *')

    elif userChoice == 7:     # CHF

        try:
            value = float(input('Enter value to convert: '))
            print()
        except ValueError:
            print()
            print('* Enter numbers only *')
            continue

        if value > 0:

            chfUsd = converter.convert('CHF', 'USD', value)
            chfEur = converter.convert('CHF', 'EUR', value)
            chfJpy = converter.convert('CHF', 'JPY', value)
            chfGbp = converter.convert('CHF', 'GBP', value)
            chfAud = converter.convert('CHF', 'AUD', value)
            chfCad = converter.convert('CHF', 'CAD', value)

            print(f'{value} Fr = {chfUsd} $')
            print(f'{value} Fr = {chfEur} €')
            print(f'{value} Fr = {chfJpy} ¥')
            print(f'{value} Fr = {chfGbp} £')
            print(f'{value} Fr = {chfAud} AU$')
            print(f'{value} Fr = {chfCad} CA$')

        else:
            print('* Enter value bigger than 0 *')

    else:
        print('* Enter number 1 - 7 *')