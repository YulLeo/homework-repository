import pytest

from homework6.task01 import instances_counter


@pytest.fixture()
def user():
    class User:
        pass
    return instances_counter(User)


def test_cls_instance(user):
    user1, _, _ = user(), user(), user()
    assert user1.get_created_instances() == 3


def test_cls_positive(user):
    assert user.get_created_instances() == 0


def test_cls_reset(user):
    user2, _, _ = user(), user(), user()
    user.reset_instances_counter() == 3
    user2.reset_instances_counter() == 0
