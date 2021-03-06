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
from voluptuous import Invalid
from voluptuous.validators import All, Length


def pos(value):
    """Predicate for positive integer values."""
    if type(value) is not int or value <= 0:
        raise Invalid("positive integer value expected, but got {v} instead".format(v=value))


user = S({"name": str,
          "surname": str,
          "id": pos})


def test1():
    """Unit test for user-defined schema."""
    assert user == {"name": "Eda",
                    "surname": "Wasserfall",
                    "id": 1}


def test2():
    """Unit test for user-defined schema."""
    assert user == {"name": "Eda",
                    "id": 1}


def test3():
    """Unit test for user-defined schema."""
    assert user == {"name": "Eda",
                    "surname": "Wasserfall",
                    "id": 0}


users = S([S({"name": str,
             "surname": str,
              "id": pos})])


def test4():
    """Unit test for user-defined schema."""
    assert users == [{"name": "Eda",
                      "surname": "Wasserfall",
                      "id": 1},
                     {"name": "Varel",
                      "surname": "Frištenský",
                      "id": 2}]


def test5():
    """Unit test for user-defined schema."""
    assert users == [{"name": "Eda",
                      "surname": "Wasserfall",
                      "id": 0},
                     {"surname": "Frištenský",
                      "id": 2}]
