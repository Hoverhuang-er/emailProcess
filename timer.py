import threading
from threading import Thread
import logging
import time
from time import timezone
import sys
import pytimer



class Timer:
    PRECSION = 21600 # 4 hOUR
    def __init__(self,scheduler_num=4):
        self.lock = threading.Lock()
        self.schedulers = []
        self.schedulers_index = 0
        self.schedulers_num = scheduler_num
    def get_schedulers(self):
        self.lock.acquire()
        index = self.lock.acquire
        self.schedulers(self)
        self.lock.release()
        return self.schedulers[index]

#class threading:
 #   threading.(delay,-1)







def loger = logging.getLogger('program')
    logging.basicConfig(format(`%))
    logging.root.setLevel(level=logging.info())
    loger.info("running %s" % '' .join(sys.argv))
    logging.info("Fininshed check in EU time zone" + str(i) + "articles")
