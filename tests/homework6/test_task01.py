import pytest

from homework6.task01 import instances_counter


@pytest.fixture()
def decorated_user():
    @instances_counter
    class User:
        pass
    return User


@pytest.fixture()
def another_decorated_class():
    @instances_counter
    class AnotherClass:
        pass
    return AnotherClass

def test_cls_instance(decorated_user):
    user1, _, _ = decorated_user(), decorated_user(), decorated_user()
    assert user1.get_created_instances() == 3


def test_cls_positive(decorated_user):
    assert decorated_user.get_created_instances() == 0


def test_cls_reset(decorated_user):
    user2, _, _ = decorated_user(), decorated_user(), decorated_user()
    assert decorated_user.reset_instances_counter() == 3
    assert user2.get_created_instances() == 0


def test_inheritance(decorated_user):
    class Something(decorated_user):
        pass

    assert Something.get_created_instances() == 0
    user2 = Something()
    assert user2.get_created_instances() == 1
    user3 = Something()
    assert user3.get_created_instances() == 2
    assert decorated_user.get_created_instances() == 0
    assert Something.get_created_instances() == 2


def test_different_counters_for_different_classes(decorated_user, another_decorated_class):
    user = decorated_user()
    user1 = decorated_user()
    another_class = another_decorated_class()
    assert another_decorated_class.get_created_instances() == 1
    assert decorated_user.get_created_instances() == 2
