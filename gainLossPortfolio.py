from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest

api_key = 'PKZ40F87LMZ0SRE16MRD' 
secret_key = 'ofkfqh8zB8JC3mz21oNAVHuVbsmfuPKxL8yUah7L'
trading_client = TradingClient(api_key, secret_key)

# Get our account information.
account = trading_client.get_account()

# Check our current balance vs. our balance at the last market close
balance_change = float(account.equity) - float(account.last_equity)
print(f'Today\'s portfolio balance change: ${balance_change}')