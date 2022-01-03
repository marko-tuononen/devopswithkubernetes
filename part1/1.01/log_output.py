import logging
import uuid
import time

DELAY = 5.0

random_str = str(uuid.uuid4())
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

while True:
    logging.info(random_str)
    time.sleep(DELAY)