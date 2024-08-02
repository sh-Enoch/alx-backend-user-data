#!/usr/bin/env python3
"""Encrypting passwords."""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hash password."""
    passwd = password.encode('utf-8')
    hashed = bcrypt.hashpw(passwd, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check password."""
    password = password.encode('utf-8')
    if bcrypt.checkpw(password, hashed_password):
        return True
