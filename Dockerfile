FROM python:3.10.6-alpine AS BUILDER
LABEL stage=BUILDER
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.10.6-alpine
RUN addgroup apprunner && adduser apprunner -D -H -G apprunner
USER apprunner
WORKDIR /app
COPY --from=BUILDER /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --chown=apprunner:apprunner ./binance ./binance

ENV PYTHONPATH="${PYTHONPATH}:/app/binance" \
    REDIS_SERVER_ADDRESS=127.0.0.1 \
    REDIS_SERVER_PORT=6379 \
    EXCHANGE_TRANSFORMATIONS_KEY=binance:transformation:mv:exchange \
    INFLUXDB_SERVER_ADDRESS=127.0.0.1 \
    INFLUXDB_SERVER_PORT=8086 \
    INFLUXDB_AUTH_TOKEN=q3cfJCCyfo4RNJuyg72U-3uEhrv3qkKQcDOesoyeIDg2BCUpmn-mjReqaGwO7GOebhd58wYVkopi5tcgCj8t5w== \
    INFLUXDB_AUTH_ORG=persuader-technology \
    INFLUXDB_BUCKET=automata \
    EXCHANGE_RATE_TIMESERIES_KEY=exchange-rate \
    MISSING_KEY=binance:mv:missing \
    VERSION=0.1 \
    PROCESS_RUN_PROFILE_KEY=binance:process:mv:run-profile \
    PROCESS_KEY=binance:process:mv:status

CMD ["python", "binance/__main__.py"]
