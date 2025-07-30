from colorama import Fore, Back, Style, init
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest

api_key = 'PKZ40F87LMZ0SRE16MRD' 
secret_key = 'ofkfqh8zB8JC3mz21oNAVHuVbsmfuPKxL8yUah7L'

trading_client = TradingClient(api_key, secret_key)

# Get our account information.
account = trading_client.get_account()

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we can use to open new positions.
print("\n")
print(Style.BRIGHT + Fore.RED + '${} is available as buying power.'.format(account.buying_power) + Style.RESET_ALL)
print("\n")
