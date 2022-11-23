import time
from logger import logging
def show_time(sttime,entime,op=""):
    logging.info(f"sttime: {entime}")
    logging.info(f"entime: {sttime}")
    logging.info(f"Delta: {entime - sttime} secs for op: {op}")

    return entime - sttime