#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""CookieSessionStore is Cookie based Sessions for ApiStar."""


import contextlib
import json
import os
import typing
from base64 import urlsafe_b64encode
from secrets import token_urlsafe

from apistar import http
from apistar.interfaces import SessionStore
from cryptography.fernet import Fernet
from werkzeug.http import dump_cookie, parse_cookie


__version__ = "1.1.0"
__all__ = ('CookieSessionStore', 'init_cookie_session')


# The Key must be 32 url-safe, base64, of Type bytes or str (UTF-8).
# default_cipher_key = 'hdJOXy9nenVk3vllaxtbM7WyUL3UaykReMgrkCnmyxc='
default_cipher_key = urlsafe_b64encode(token_urlsafe(24).encode("utf-8"))
cipher = Fernet(os.getenv('APISTAR_SESSION_CIPHER_KEY', default_cipher_key))


class CookieSessionStore(SessionStore):

    """Cookie based Sessions for ApiStar."""

    cookie_name = 'session'

    def new(self) -> http.Session:
        return http.Session(session_id='')

    def load(self, session_data: str) -> http.Session:
        try:
            data = json.loads(cipher.decrypt(str.encode(session_data)))
        except (ValueError, Exception):
            return self.new()
        return http.Session(session_id='', data=data)

    def save(self, session: http.Session) -> dict:
        data = cipher.encrypt(str.encode(json.dumps(session.data)))
        cookie = dump_cookie(self.cookie_name, data)
        return {'Set-Cookie': cookie}


@contextlib.contextmanager
def init_cookie_session(cookie: http.Header,
                        response_headers: http.ResponseHeaders) -> typing.Generator[http.Session, None, None]:
    """Initialize a CookieSessionStore."""
    cookies = parse_cookie(cookie)
    session_data = cookies.get(CookieSessionStore.cookie_name)
    if session_data:
        session = CookieSessionStore().load(session_data)
    else:
        session = CookieSessionStore().new()
    try:
        yield session
    finally:
        session_headers = CookieSessionStore().save(session)
        response_headers.update(session_headers)
