import logging
import os
from cgitb import handler


def setup_logger(name="api_test_logger"):
    os.makedirs("logs",exist_ok=True)
    logger=logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler= logging.FileHandler("logs/api_test.log")
    formatter=logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger