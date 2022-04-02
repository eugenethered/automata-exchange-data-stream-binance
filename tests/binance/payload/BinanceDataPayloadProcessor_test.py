import unittest

from data.message.DataMessageProcessor import DataMessageProcessor

from binance.payload.BinanceDataPayloadProcessor import BinanceDataPayloadProcessor


class BinanceDataPayloadProcessorTestCase(unittest.TestCase):

    def test_process_message_in_payload(self):
        payload = '{' \
                  '"stream":"!ticker@arr",' \
                  '"data":[' \
                  '{' \
                  '"e":"24hrTicker",' \
                  '"E":1648913430060,' \
                  '"s":"BTCUSDT",' \
                  '"p":"-71.76000000",' \
                  '"P":"-0.154",' \
                  '"w":"46472.77080038",' \
                  '"x":"46560.65000000",' \
                  '"c":"46488.89000000",' \
                  '"Q":"0.04087000",' \
                  '"b":"46491.59000000",' \
                  '"B":"0.03226400",' \
                  '"a":"46491.60000000",' \
                  '"A":"0.04280400",' \
                  '"o":"46560.65000000",' \
                  '"h":"95000.00000000",' \
                  '"l":"44477.76000000",' \
                  '"v":"2564.68508800",' \
                  '"q":"119188022.26977675",' \
                  '"O":1648827026946,' \
                  '"C":1648913426946,' \
                  '"F":4732465,' \
                  '"L":4840067,' \
                  '"n":107603' \
                  '}]' \
                  '}'
        message_processor = TestAccumulatingDataMessageProcessor()
        payload_processor = BinanceDataPayloadProcessor(message_processor)
        payload_processor.process_payload(payload)
        expected_message = {
            'A': '0.04280400',
            'B': '0.03226400',
            'C': 1648913426946,
            'E': 1648913430060,
            'F': 4732465,
            'L': 4840067,
            'O': 1648827026946,
            'P': '-0.154',
            'Q': '0.04087000',
            'a': '46491.60000000',
            'b': '46491.59000000',
            'c': '46488.89000000',
            'e': '24hrTicker',
            'h': '95000.00000000',
            'l': '44477.76000000',
            'n': 107603,
            'o': '46560.65000000',
            'p': '-71.76000000',
            'q': '119188022.26977675',
            's': 'BTCUSDT',
            'v': '2564.68508800',
            'w': '46472.77080038',
            'x': '46560.65000000'
        }
        self.assertEqual(1, len(message_processor.messages), 'Payload should have 1 message')
        self.assertEqual(expected_message, message_processor.messages[0])


# test class for simple message holding
class TestAccumulatingDataMessageProcessor(DataMessageProcessor):

    def __init__(self):
        self.messages = []

    def process_message(self, message):
        self.messages.append(message)


if __name__ == '__main__':
    unittest.main()
