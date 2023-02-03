#!/usr/bin/env python3
"""
function called filter_datum that returns the log message obfuscated
"""
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ filter values in incoming log records"""
        record.message = self.filter_datum(record.getMessage())
    return super().format(record)

    def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
     returns the log message obfuscated
    """
    for field in fields:
        message = re.sub(fr'{field}=(.+?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message