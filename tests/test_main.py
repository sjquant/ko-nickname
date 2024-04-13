import random
from konickname import generate_nickname
import re


def test_sut_works():
    random.seed(42)
    nickname = generate_nickname()

    assert nickname == "빛나는호랑이4506"


def test_sut_makes_specified_digits():
    nickname = generate_nickname(digits=5)

    matched = re.search(r"\d+", nickname)

    assert len(matched.group()) == 5


def test_sut_makes_different_nicknames_each_time():
    random.seed(42)
    nickname1 = generate_nickname()
    nickname2 = generate_nickname()

    assert nickname1 != nickname2
