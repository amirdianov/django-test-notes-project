import pytest

from web.tests.factories import NoteFactory, UserFactory


@pytest.fixture(autouse=True)
def init_db(db):
    pass


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def note(user):
    return NoteFactory(user=user)
