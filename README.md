# automata-data-stream-binance
Automata Binance Data Stream

## Packaging
`python3 -m build`

## Clean the build
`rm -fr dist automata.data.stream.binance.egg-info`

## Running

### IDE
1. Go to `Run`
2. Choose `Edit configurations...`
3. In `Paramaters:` 
   ```
   wss://testnet.binance.vision/stream?streams=!ticker@arr --options MESSAGE_TRANSFORM_RULES_KEY=binance:message:transform-rules REDIS_SERVER_ADDRESS=192.168.1.90 REDIS_SERVER_PORT=6379
   ```