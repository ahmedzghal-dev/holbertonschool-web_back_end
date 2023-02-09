#!/usr/bin/env python3
""" Session Auth class """

from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)


class SessionAuth(Auth):
    """ My SessionAuth class """
    if os.environ.get('AUTH_IMPLEMENTATION') == 'SESSION':
        auth = SessionAuth()
    else:
        auth = Auth()
