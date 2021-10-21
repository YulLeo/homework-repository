import pytest
from bs4 import BeautifulSoup

from homework10.task01 import get_high_52, get_low_52, get_p_e, get_price


@pytest.fixture()
def beautiful_soup_object():
    with open('example_company_page.html', 'r') as html_doc:
        soup = BeautifulSoup(html_doc, 'html.parser')
        return soup


def test_get_price(beautiful_soup_object):
    assert get_price(beautiful_soup_object) == 45338.38


def test_get_high_52(beautiful_soup_object):
    assert get_high_52(beautiful_soup_object) == 673.88


def test_get_low_52(beautiful_soup_object):
    assert get_low_52(beautiful_soup_object) == 420.78


def test_get_p_e(beautiful_soup_object):
    assert get_p_e(beautiful_soup_object) == 47.10
