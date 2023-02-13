#!/usr/bin/env python3
"""
Auth class
"""
from flask import request
from typing import List, TypeVar
import os
sesion_name = os.getenv("SESSION_NAME")


class Auth():
    """
    auth class description
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require auth function
        Define which routes don't need authentication
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        for excluded_path in excluded_paths:
            if path == excluded_path or path.startswith(excluded_path[:-1]):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        authorization_header function
        """
        if request is None:
            return None
        if "Authorization" not in request.headers:
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """
        get current user function
        """

        return None

    def session_cookie(self, request=None):
        """ Session cookie
        returns a cookie value from a request
        """
        if request is None:
            return None
        if sesion_name is None:
            return None
        return request.cookies.get(sesion_name)
