#!/usr/bin/env python3
""" SessionAuth class to manage API authentication """


from flask import request
from api.v1.auth.auth import Auth
from models.user import User
import uuid
from typing import List, TypeVar
import base64


class SessionAuth(Auth):
    """1. Empty session
    Args:
        Auth (_class_): inherits from class Auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """_summary_
        Args:
            user_id (str, optional): _description_. Defaults to None.
        Returns:
            str: _description_
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """_summary_
        Args:
            session_id (str, optional): _description_. Defaults to None.
        Returns:
            str: _description_
        """
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ returns
        a User instance based on a cookie value
        """
        sessions = self.session_cookie(request)
        user_id = self.user_id_for_session_id(sessions)
        return User.get(user_id)
