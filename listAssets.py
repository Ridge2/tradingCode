from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass

api_key = 'PKZ40F87LMZ0SRE16MRD' 
secret_key = 'ofkfqh8zB8JC3mz21oNAVHuVbsmfuPKxL8yUah7L'

trading_client = TradingClient(api_key, secret_key)

# search for US equities
search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)

assets = trading_client.get_all_assets(search_params)