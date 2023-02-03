#!/usr/bin/env python3
"""
function called filter_datum that returns the log message obfuscated
"""
import re
from typing import List
import logging

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filters values from the log record"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)

    def filter_datum(fields: List[str], redaction: str, message: str,
                     separator: str) -> str:
        """returns log message obfuscated"""
        for field in fields:
            message = re.sub(f'{field}=(.*?){separator}',
                             f'{field}={redaction}{separator}', message)
        return message

    def get_logger() -> logging.Logger:
        """ takes no arguments and returns
        a logging.Logger object"""
        logger = logging.getLogger("user_data")
        logger.setLevel(logging.INFO)
        logger.propagate = False
        formatter = RedactingFormatter(PII_FIELDS)
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger
