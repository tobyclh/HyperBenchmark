import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from queue import Queue
from time import sleep
from .GoogleLogHandler import GoogleLogHandler
from threading import Thread


_default_attri = ['levelname', 'module', 'msg', 'name']


class GoogleLog:
    def __init__(self, name='new_sheet', sheet_id=None, update_interval=5, **kwargs):
        """Google Log allows easy logging to google sheet
        
        Parameters
        ----------
        name : str, optional
            [description] (the default is 'new_sheet', which [default_description])
        sheet_id : [type], optional
            [description] (the default is None, which [default_description])
        update_interval : int, optional
            write to the sheet once every approximately # seconds, Google Sheet API is limited to 100 write / 100 secs per key.
        """
        self.sheet_id = sheet_id
        self.sheet_name = name
        self.msg_queue = Queue()
        self.update_interval = update_interval
        self._handler = GoogleLogHandler(self)
        self.attris = kwargs['attri'] if 'attri' in kwargs.keys() else _default_attri
        self.addi_attris = kwargs['addi_attris'] if 'addi_attris' in kwargs.keys() else {}
        self._should_stop = False
        self.thread = Thread(target=self._write_message)
        self.thread.daemon = True
        self.thread.start() # the thread dies with this program

    @property
    def handler(self):
        return self._handler
    
    def _write_message(self):
        # print('thread started')
        while not self._should_stop:
            while not self.msg_queue.empty():
                record = self.msg_queue.get()
                data = {}
                for attr in self.attris:
                    data[attr] = getattr(record, attr)
                data.update(self.addi_attris)
                for key, value in data.items():
                    print(f'Key : {key} value : {value}')
            sleep(self.update_interval)
    
    def __del__(self):
        self._should_stop = True
        self.thread.join(timeout=self.update_interval+1)

    def append(self, msg):
        self.msg_queue.put(msg)
        return