#!/usr/bin/env python3
"""Hash password."""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Take a password and return bytes."""
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed
