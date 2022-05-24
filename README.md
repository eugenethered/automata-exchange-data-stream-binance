# Automata Binance Exchange Data Stream

## Packaging
`python3 -m build`

## Dependencies (IDE Terminal)
`pip install persuader-technology-automata-core persuader-technology-automata-data.stream persuader-technology-automata-exchange-repository persuader-technology-automata-config`

## Running

### IDE
1. Go to `Run`
2. Choose `Edit configurations...`
3. In `Paramaters:` 
   ```
   wss://testnet.binance.vision/stream?streams=!ticker@arr  
   --options 
     REDIS_SERVER_ADDRESS=192.168.1.90 
     REDIS_SERVER_PORT=6379 
     EXCHANGE_TRANSFORMATIONS_KEY=binance:exchange:transformations 
     EXCHANGE_RATE_TIMESERIES_KEY=binance:time-series:exchange-rate:{}  
     EXCHANGE_RATE_TIMESERIES_RETENTION=360000 
     MISSING_KEY=binance:missing
     PROCESS_KEY={}:process:status:{} 
     PROCESS_RUN_PROFILE_KEY={}:process:run-profile:{} 
   ```

## Environments

### Test
wss://testnet.binance.vision

### Live
wss://stream.binance.com:9443
