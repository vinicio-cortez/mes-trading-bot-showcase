# MES Futures Trading Bot (ICT/SMC)

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://python.org)
[![IBKR](https://img.shields.io/badge/IBKR-TWS%20API-green)](https://interactivebrokers.com)
[![Status](https://img.shields.io/badge/Status-Paper%20Trading-brightgreen)](https://github.com/vinicio-cortez)

## Overview

Automated trading system for MES (Micro E-mini S&P 500) futures using ICT Smart Money Concepts methodology.

### Features
- Multi-timeframe analysis (30m bias + 5m entries)
- Fair Value Gap (FVG) detection
- Liquidity sweep identification
- Break of Structure / Change of Character (BOS/CHOCH)
- Equal Highs / Equal Lows (EQH/EQL)
- Kill Zone session filters
- Automated bracket orders via Interactive Brokers API
- Fixed fractional risk management

### Technology Stack
| Component | Technology |
|-----------|------------|
| Language | Python 3.12 |
| Broker API | Interactive Brokers (ib_insync) |
| Data Processing | pandas, numpy |
| SMC Patterns | smartmoneyconcepts |
| Environment | WSL2 Ubuntu 24.04 |

### Architecture Flow

Main Controller (Kill Zones, Session Management)
                    |
    +---------------+---------------+
    |                               |
Data Fetcher                   Bias Detector
(IBKR API)                     (30m Chart)
    |                               |
    +---------------+---------------+
                    |
              SMC Scanner
              (5m Chart)
                    |
              Order Manager
              (Bracket OCO)

### Performance Metrics
*Metrics from paper trading - April 2026*

| Metric | Value |
|--------|-------|
| Instrument | MES Futures |
| Timeframe | 30m bias / 5m entry |
| Risk per trade | $50 |
| Max drawdown | *Collecting data* |
| Win rate | *Collecting data* |
| Profit factor | *Collecting data* |

### Demo
*[Screenshot or GIF of bot running]*

### Configuration Example
```python
# config.example.py - Safe to share
INSTRUMENT = "MES"
TIMEFRAME_BIAS = "30 mins"
TIMEFRAME_ENTRY = "5 mins"
RISK_PER_TRADE = 50.0
MAX_POSITION_SIZE = 1

# Kill Zones (EST)
TRADE_SESSIONS = {
    "London": ("02:00", "05:00"),
    "New_York_AM": ("08:30", "11:00"),
    "New_York_PM": ("13:30", "16:00"),
}
Licensing & Access
The core trading strategy and implementation are proprietary and available for licensing.

For inquiries: Contact via GitHub

Available For
Strategy licensing

Custom development

Consulting engagements

© 2026 Vinicio Cortez - All Rights Reserved
