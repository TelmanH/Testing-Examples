import requests

rates_cache = {}
cur_to_exchange = input().lower()
r = requests.get(f"http://www.floatrates.com/daily/{cur_to_exchange}.json")

if r:
    r = r.json()
    if cur_to_exchange == 'usd':
        rates_cache['eur'] = r['eur']['rate']
    elif cur_to_exchange == 'eur':
        rates_cache['usd'] = r['usd']['rate']
    else:
        rates_cache['usd'] = r['usd']['rate']
        rates_cache['eur'] = r['eur']['rate']

    cur_request = input().lower()

    while cur_request:
        cur_amt = float(input())
        print("Checking the cache...")
        if cur_request in rates_cache:
            print("Oh! It is in the cache!")
            print(f"You received {round(cur_amt * rates_cache[cur_request], 2)} {cur_request.upper()}.")

        else:
            print("Sorry, but it is not in the cache!")
            rates_cache[cur_request] = r[cur_request]['rate']
            print(f"You received {round(cur_amt * rates_cache[cur_request], 2)} {cur_request.upper()}.")

        cur_request = input().lower()