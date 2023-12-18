import argparse
import logging

FORMAT = '{levelname} - {asctime} - {msg}'
logging.basicConfig(level=logging.INFO, filename='my_func.log', encoding='utf-8',
                    format=FORMAT, style='{')
logger = logging.getLogger(__name__)


def get_number(number: int, mod: int = 10) -> str:

    result = ''
    if mod < 0:
        logger.error(f'Number system {mod} does not exist')
        return float('inf')
    while number != 0:
        try:
            result = str(number % mod) + result
            number //= mod
        except ZeroDivisionError as e:
            logger.error(f'Number system {mod} does not exist')
            return float('inf')
    logger.info(f'{number}, {mod} = {result}')
    return result


def parser_func():
    parser = argparse.ArgumentParser(description='Getting arguments from a string')
    parser.add_argument('--number')
    parser.add_argument('--mod', default=10)
    args = parser.parse_args()
    print(args)
    return get_number(int(args.number), int(args.mod))


if __name__ == '__main__':
    print(get_number(1234123, 2))
    print(get_number(1234123, 0))
    print(get_number(1234123, -2))
    parser_func()



