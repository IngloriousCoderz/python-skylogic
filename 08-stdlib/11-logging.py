import logging

# Try without and with this line, which must be at the top
# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

logging.debug('Debug message')
logging.info('Informational message')
logging.warning('Potential issues')
logging.error('An error occurred')
logging.critical('This is bad, shutting down')

# For extra logging features @see https://docs.python.org/3/howto/logging.html
