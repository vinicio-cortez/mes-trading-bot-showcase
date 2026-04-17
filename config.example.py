"""
Configuration Example - MES Trading Bot
Safe for public viewing - no actual credentials.
"""

INSTRUMENT = "MES"
EXCHANGE = "CME"
CURRENCY = "USD"

TIMEFRAME_BIAS = "30 mins"
TIMEFRAME_ENTRY = "5 mins"

RISK_PER_TRADE = 50.0
MAX_POSITION_SIZE = 1

TWS_HOST = "127.0.0.1"
TWS_PORT = 7497
TWS_CLIENT_ID = 1

TRADE_SESSIONS = {
    "London": ("02:00", "05:00"),
    "New_York_AM": ("08:30", "11:00"),
    "New_York_PM": ("13:30", "16:00"),
}
