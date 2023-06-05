from dataclasses import dataclass

import pytest


@dataclass
class User:
    username: str


class InMemoryUserRepository:
    def __init__(self) -> None:
        self._users = []

    def add(self, user: User) -> None:
        self._users.append(user)

    def get_by_username(self, username: str) -> User:
        return next(user for user in self._users if user.username == username)


# BAD - depends on persistance layer having user record at test time
def test_get_by_username():
    user = User(username="someone@gmail.com")
    repository = InMemoryUserRepository()
    assert repository.get_by_username(user.username) == user


# BAD - test_user_is_fetched_by_username will succeed only when running after test_added_user
@pytest.fixture(scope="module")
def repository():
    return InMemoryUserRepository()


def test_added_user(repository):
    user = User(username="someone@gmail.com")
    assert repository.add(user) is None


def test_user_is_fetched_by_username(repository):
    user = User(username="someone@gmail.com")
    assert repository.get_by_username(user.username) == user


# GOOD - makes sure it has all the needed data
def test_added_user_is_fetched_by_username():
    user = User(username="someone@gmail.com")
    repository = InMemoryUserRepository()
    repository.add(user)
    assert repository.get_by_username(user.username) == user
