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
        """

        return False

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
