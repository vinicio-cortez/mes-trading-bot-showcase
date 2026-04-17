# System Architecture

## Data Flow
1. TWS API streams real-time MES data
2. 30m bars feed into Bias Detector
3. 5m bars feed into SMC Scanner
4. Confluence check validates setups
5. Order Manager executes bracket orders

## Components
- DataFetcher: IBKR connection, historical/real-time bars
- BiasDetector: 3-bar volume expansion on 30m
- SMCScanner: FVG, liquidity, BOS/CHOCH, EQH/EQL
- OrderManager: Bracket OCO orders, risk sizing
