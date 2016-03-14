__author__ = 'nacim'

from urllib3.util import parse_url
from urllib3.exceptions import LocationParseError

secure_protocol = ['https', 'ssl', 'ssh', 'sftp', 'ftps']

def is_secure(value):
    return value in secure_protocol

def urlparsing(value):
    try:
        loc = parse_url(value)
    except LocationParseError as error:
        return None, None, None

    return is_secure(loc.scheme), loc.host, loc.port



