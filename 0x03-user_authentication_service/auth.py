#!/usr/bin/env python3
"""Hash password."""
import bcrypt
from user import User
from db import DB


def _hash_password(password: str) -> bytes:
    """Take a password and return bytes."""
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        """Initialize class."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Return a user object."""
        if email and password:
            try:
                usr = self._db.find_user_by(email=email)
                if usr:
                    raise ValueError("User {} already exists".format(email))
            except ValueError:
                raise ValueError("User {} already exists".format(email))
            password = _hash_password(password)
            user = self._db.add_user(email, password)
            return user
