# Automata Binance Data Stream

## Packaging
`python3 -m build`

## Dependencies (IDE Terminal)
`pip install persuader-technology-automata-core persuader-technology-automata-utilities persuader-technology-automata-redis persuader-technology-automata-data.stream`

## Running

### IDE
1. Go to `Run`
2. Choose `Edit configurations...`
3. In `Paramaters:` 
   ```
   wss://testnet.binance.vision/stream?streams= --options REDIS_SERVER_ADDRESS=192.168.1.90 REDIS_SERVER_PORT=6379 EXCHANGE_TRANSFORMATION_RULES_KEY=binance:exchange:transform-rules EXCHANGE_RATE_TIMESERIES_KEY=binance:time-series:exchange-rate:{}
   ```