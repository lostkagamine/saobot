# generic logging lib for saobot

from enum import Enum
import datetime

class LogType(Enum):
    CRITICAL = '[CRITICAL] '
    ERROR = '[Error!] '
    WARNING = '[Warn] '
    INFO = '[i] '
    LOG = ''

def log(msg, ltype:LogType=LogType.LOG):
    print(f'[{datetime.datetime.utcnow()}]{ltype.value}{msg}')
