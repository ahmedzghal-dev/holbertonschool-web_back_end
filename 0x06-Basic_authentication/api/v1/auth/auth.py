#!/usr/bin/env python3
"""
Auth class
"""
from flask import request
from typing import List, TypeVar


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

        if not excluded_paths or not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            if path == excluded_path or path.startswith(excluded_path[:-1]):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        authorization_header function
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        get current user function
        """

        return None
