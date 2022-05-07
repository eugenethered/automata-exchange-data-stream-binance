import logging

from cache.holder.RedisCacheHolder import RedisCacheHolder
from core.arguments.command_line_arguments import url_option_arg_parser

from binance.BinanceExchangeDataStream import BinanceExchangeDataStream

if __name__ == '__main__':
    command_line_arg_parser = url_option_arg_parser()
    args = command_line_arg_parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    logging.info(f'Binance Exchange Data Stream starting with URL {args.url} OPTIONS {args.options}')

    RedisCacheHolder(args.options)

    data_stream = BinanceExchangeDataStream(args.url, args.options)
    data_stream.receive_data()
