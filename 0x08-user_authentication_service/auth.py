#!/usr/bin/env python3
"""AUTH module"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ takes in a password string
    arguments and returns bytes"""
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ register user """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode(), user.hashed_password)

    def valid_login(self, email, password) -> bool:
        """login"""
        user = self._db.get_user(email)
        if user:
            hashed_password = user["password"].encode('utf-8')
            password = password.encode('utf-8')
            return bcrypt.checkpw(password, hashed_password)
        else:
            return False
