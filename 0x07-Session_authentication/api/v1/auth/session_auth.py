#!/usr/bin/env python3
""" Session Auth class """


class SessionAuth(Auth):
    """ My SessionAuth class """
    if os.environ.get('AUTH_IMPLEMENTATION') == 'SESSION':
        auth = SessionAuth()
    else:
        auth = Auth()
