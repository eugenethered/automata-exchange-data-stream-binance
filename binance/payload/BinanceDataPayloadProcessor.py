from data.payload.DataPayloadProcessor import DataPayloadProcessor


class BinanceDataPayloadProcessor(DataPayloadProcessor):

    def process_payload(self, payload):
        print(f'payload -> {payload}')
