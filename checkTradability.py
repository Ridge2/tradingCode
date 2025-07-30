from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest

api_key = 'PKZ40F87LMZ0SRE16MRD' 
secret_key = 'ofkfqh8zB8JC3mz21oNAVHuVbsmfuPKxL8yUah7L'
trading_client = TradingClient(api_key, secret_key)

# search for PLTR
aapl_asset = trading_client.get_asset('PLTR')

if aapl_asset.tradable:
    print('We can trade PLTR')