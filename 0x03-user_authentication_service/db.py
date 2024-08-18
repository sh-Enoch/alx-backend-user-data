#!/usr/bin/env python3
"""Implement add_user method."""

from sqlalchemy import create_engine, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy .exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base
from user import User


class DB():
    """DB class."""

    def __init__(self) -> None:
        """Initialize a new DB instance."""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object."""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Save user to the database."""
        user = User(email=email, hashed_password=hashed_password)
        session = self._session
        session.add(user)
        session.commit()
        return user

    def find_user_by(self, **kwargs):
        """Filter users."""
        session = self._session
        try:
            user = session.query(User).filter_by(**kwargs).one()
            return user
        except InvalidRequestError:
            print("Invalid")
        except NoResultFound:
            print("Not found")

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update user."""
        if user_id:
            session = self._session
            try:
                user = self.find_user_by(id=user_id)
                stmt = update(User).where(User.id == user_id).values(**kwargs)
                session.execute(stmt)
                session.commit
                return user
            except ValueError:
                print("Error")
