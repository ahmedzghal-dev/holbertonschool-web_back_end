#!/usr/bin/env python3
"""
BasicAuth class
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar, Tuple
from models.user import User


class BasicAuth(Auth):
    """
    empty class
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        extract base64 here
        """
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split("Basic ")[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        function to decode base64
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            code = base64_authorization_header.encode('utf-8')
            decoded = base64.b64decode(code)
            return decoded.decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """
        function to extract user credentails
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        try:
            email, password = decoded_base64_authorization_header.split(":", 1)
            return email, password
        except ValueError:
            return None, None

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """
        user object from credentails
        """
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        for i in users:
            if i.is_valid_password(user_pwd):
                return i
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        get current user details
        """
        autorization = self.authorization_header(request)
        base64 = self.extract_base64_authorization_header(autorization)
        decode = self.decode_base64_authorization_header(base64)
        user_email, user_password = self.extract_user_credentials(decode)
        return self.user_object_from_credentials(user_email, user_password)
