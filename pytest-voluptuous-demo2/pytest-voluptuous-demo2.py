#!/usr/bin/env python
# vim: set fileencoding=utf-8

from pytest_voluptuous import S, Partial, Exact
from voluptuous import Invalid
from voluptuous.validators import All, Length


def pos(value):
    if type(value) is not int or value <= 0:
        raise Invalid("positive integer value expected, but got {v} instead".format(v=value))


user = S({"name": str,
          "surname": str,
          "id": pos})


def test1():
    assert user == {"name": "Eda",
                    "surname": "Wasserfall",
                    "id": 1}


def test2():
    assert user == {"name": "Eda",
                    "id": 1}


def test3():
    assert user == {"name": "Eda",
                    "surname": "Wasserfall",
                    "id": 0}


users = S([S({"name": str,
             "surname": str,
             "id": pos})])

def test4():
    assert users == [{"name": "Eda",
                      "surname": "Wasserfall",
                      "id": 1},
                     {"name": "Varel",
                      "surname": "Frištenský",
                      "id": 2}]

def test5():
    assert users == [{"name": "Eda",
                      "surname": "Wasserfall",
                      "id": 0},
                     {"surname": "Frištenský",
                      "id": 2}]
