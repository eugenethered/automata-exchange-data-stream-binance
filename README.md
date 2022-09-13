# Automata Binance Exchange Data Stream

## Docker
1. `docker build . -t persuadertechnology/automata-exchange-data-stream:binance-0.1`
2. `docker image prune --filter label=stage=BUILDER`

## Publishing to Docker Repository
todo: automate this...
1. `docker push persuadertechnology/automata-exchange-data-stream:binance-0.1`

## Publishing Prerequisites
Need to log in to via docker cli i.e. `docker login -u`

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
     INFLUXDB_SERVER_ADDRESS=127.0.0.1 \
     INFLUXDB_SERVER_PORT=8086 \
     INFLUXDB_AUTH_TOKEN=q3cfJCCyfo4RNJuyg72U-3uEhrv3qkKQcDOesoyeIDg2BCUpmn-mjReqaGwO7GOebhd58wYVkopi5tcgCj8t5w== \
     INFLUXDB_AUTH_ORG=persuader-technology \
     INFLUXDB_BUCKET=automata \
     EXCHANGE_RATE_TIMESERIES_KEY=exchange-rate  
     MISSING_KEY=binance:missing
     PROCESS_KEY={}:process:status:{} 
     PROCESS_RUN_PROFILE_KEY={}:process:run-profile:{} 
   ```

## Environments

### Test
wss://testnet.binance.vision

### Live
wss://stream.binance.com:9443
