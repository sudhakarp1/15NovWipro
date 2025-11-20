import logging

logging.basicConfig(
                    filename='testLog.log',
                    filemode='a',
                    level=logging.DEBUG, 
                    format='%(asctime)s: %(levelname)s: %(message)s'
                    )

logging.info('Starting my Program')
logging.warning('Just a message to test')
logging.debug('Just a DEBUG message to test')
logging.error('Just a message to test')
