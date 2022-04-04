from binance.BinanceDataStream import BinanceDataStream
from binance.arguments.command_line_arguments import init_arg_parser

if __name__ == '__main__':
    command_line_arg_parser = init_arg_parser()
    args = command_line_arg_parser.parse_args()

    data_stream = BinanceDataStream(args.url, args.options)
    data_stream.receive_data()
