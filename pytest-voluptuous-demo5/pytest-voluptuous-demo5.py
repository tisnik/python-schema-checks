#!/usr/bin/env python
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2018, 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

"""Basic usage of pytest_voluptuous library in unit tests."""

from pytest_voluptuous import S, Partial, Exact
from voluptuous import Invalid, Optional, Required
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


def test4():
    assert user == {"name": "Eda",
                    "surname": "Wasserfall"}


user2 = S({"name": str,
           "surname": str,
           Optional("id"): pos})


def test5():
    assert user2 == {"name": "Eda",
                     "surname": "Wasserfall",
                     "id": 1}


def test6():
    """Unit test for the data record."""
    assert user2 == {"name": "Eda",
                     "id": 1}


def test7():
    """Unit test for the data record."""
    assert user2 == {"name": "Eda",
                     "surname": "Wasserfall",
                     "id": 0}


def test8():
    """Unit test for the data record."""
    assert user2 == {"name": "Eda",
                     "surname": "Wasserfall"}


user3 = S({"name": str,
           "surname": str,
           Optional("id"): pos,
           Optional("address"): str,
           Optional("state"): str,
           Optional("zip"): int})


def test9():
    """Unit test for the data record."""
    assert user3 == {"name": "Eda",
                     "surname": "Wasserfall",
                     "id": 1}


def test10():
    """Unit test for the data record."""
    assert user3 == {"name": "Eda",
                     "surname": "Wasserfall"}


def test11():
    """Unit test for the data record."""
    assert user3 == {"name": "Eda",
                     "surname": "Wasserfall",
                     "zip": 12345}


user4 = S({Required("name"): str,
           Required("surname"): str,
           "id": pos,
           "address": str,
           "state": str,
           "zip": int}, required=False)


def test12():
    """Unit test for the data record."""
    assert user4 == {"name": "Eda",
                     "surname": "Wasserfall",
                     "id": 1}


def test13():
    """Unit test for the data record."""
    assert user4 == {"name": "Eda",
                     "surname": "Wasserfall"}


def test14():
    """Unit test for the data record."""
    assert user4 == {"name": "Eda",
                     "surname": "Wasserfall",
                     "zip": 12345}
