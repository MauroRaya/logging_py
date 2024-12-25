#!/usr/bin/env python3
import logging
import mylib

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename='log.log', level=logging.INFO)
    logger.info('Starting execution')
    mylib.do_something()
    logger.info('Ending execution')


if __name__ == '__main__':
    main()