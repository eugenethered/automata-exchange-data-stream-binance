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
        message_processors = [message_processor]
        payload_processor = BinanceDataPayloadProcessor(message_processors)
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

    def test_process_multiple_messages_in_payload(self):
        payload = '{"stream":"!ticker@arr",' \
                  '"data":[' \
                      '{"e":"24hrTicker","E":1648913430091,"s":"BNBUSDT","p":"3.30000000","P":"0.747","w":"446.59611119","x":"441.80000000","c":"445.20000000","Q":"5.13000000","b":"445.10000000","B":"1.89000000","a":"445.20000000","A":"5.51000000","o":"441.90000000","h":"456.90000000","l":"100.00000000","v":"19922.77000000","q":"8897431.60610000","O":1648827027080,"C":1648913427080,"F":1148627,"L":1154053,"n":5427},' \
                      '{"e":"24hrTicker","E":1648913430060,"s":"BTCUSDT","p":"-71.76000000","P":"-0.154","w":"46472.77080038","x":"46560.65000000","c":"46488.89000000","Q":"0.04087000","b":"46491.59000000","B":"0.03226400","a":"46491.60000000","A":"0.04280400","o":"46560.65000000","h":"95000.00000000","l":"44477.76000000","v":"2564.68508800","q":"119188022.26977675","O":1648827026946,"C":1648913426946,"F":4732465,"L":4840067,"n":107603}' \
                  ']}'
        message_processor = TestAccumulatingDataMessageProcessor()
        message_processors = [message_processor]
        payload_processor = BinanceDataPayloadProcessor(message_processors)
        payload_processor.process_payload(payload)
        self.assertEqual(2, len(message_processor.messages), 'Payload should have 2 message')


# test class for simple message holding
class TestAccumulatingDataMessageProcessor(DataMessageProcessor):

    def __init__(self):
        super().__init__()
        self.set_listen_stream('!ticker@arr')
        self.messages = []

    def process_message(self, message):
        self.messages.append(message)


if __name__ == '__main__':
    unittest.main()
