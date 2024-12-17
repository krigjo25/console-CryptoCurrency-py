#   BitCoin Price Calculator
import sys, json, requests

def main():
    '''
        #   Title   :   Crypto Currency
        #   Description :
                Command-line program to calculate usd price for crypto currency


    '''

    try:

        #   Ensure the data provided is a number
        if len(sys.argv) != 2 or sys.argv[1].isalpha():
            raise Exception("Usage : python app.py [numeric value]")

    except Exception as e:
        sys.exit(f"{e}")

    #   Fetching the data from the api
    req = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    jsonData = json.loads(req.text)

    #   Calculating the value of the crypto currency
    usd = float(sys.argv[1])
    usd *= jsonData['bpi']['USD']['rate_float']

    print(f"${usd:,.4f}")

    return


if __name__ == '__main__':
    main()
