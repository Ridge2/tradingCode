from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

api_key = 'PKZ40F87LMZ0SRE16MRD' 
secret_key = 'ofkfqh8zB8JC3mz21oNAVHuVbsmfuPKxL8yUah7L'
trading_client = TradingClient(api_key, secret_key, paper=True)

# preparing orders
market_order_data = MarketOrderRequest(
                    symbol="SPY",
                    qty=0.01,
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.GTC
                )

# Market order
market_order = trading_client.submit_order(
                order_data=market_order_data
               )