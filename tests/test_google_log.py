from HyperBenchmark.GoogleLog import GoogleLog
import logging as log
from time import sleep
def test_sheet():
    glog = GoogleLog(cred_file='google-glog.json',name='Testing', update_interval=0.1, new_sheet=True, addi_attris={'instanceid':'123456'}, email='tobyclh@gmail.com')
    logger = log.getLogger('glog')
    logger.addHandler(glog.handler)
    logger.error('banana')
    sleep(1)
    logger.error('apple')
    sleep(1)
    logger.error('honey')
    sleep(1)
    logger.error('tiers')
    sleep(1)
    print('End')


def test_sheet_dict():
    glog = GoogleLog(cred_file='google-glog.json',name='Testing', update_interval=0.1, new_sheet=True, addi_attri={'instanceid':'123456'}, email='tobyclh@gmail.com')
    logger = log.getLogger('glog')
    logger.addHandler(glog.handler)
    logger.error({'banana':123412, 'df':'sfasd'})    
    logger.error('apple')
    logger.error('honey')
    sleep(5)
    logger.error('tiers')
    sleep(2)
    print('End')

if 'main' in __name__:
    test_sheet_dict()
