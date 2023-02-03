#!/usr/bin/env python3
"""function called filter_datum that
returns the log message obfuscated"""

import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        message = re.sub(f'{field}=(.*?){sepatator}',
                         f'{field}={redaction}{sepatator}', message)
    return message