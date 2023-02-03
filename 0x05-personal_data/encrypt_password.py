#!/usr/bin/env python3
""" function that expects one string argument
name password and returns a salted, hashed password"""

import bcrypt


def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
