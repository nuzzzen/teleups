import os
import logging

def setup_logger():
    log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ups_monitor.log')
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[logging.FileHandler(log_file),
                                  logging.StreamHandler()])
    logger = logging.getLogger(__name__)
    return logger
