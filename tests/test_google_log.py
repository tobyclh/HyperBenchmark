from HyperBenchmark.GoogleLog import GoogleLog
import logging as log
from time import sleep
def test_sheet():
    glog = GoogleLog(update_interval=3, addi_attris={'instanceid':'123456'})
    logger = log.getLogger('glog')
    logger.addHandler(glog.handler)
    logger.error('banana')
    sleep(1)
    logger.error('apple')
    sleep(1)
    logger.error('honey')
    sleep(1)
    logger.error('tiers')
    print('End')

if 'main' in __name__:
    test_sheet()
