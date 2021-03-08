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

"""Elementary usage of schemagic package."""

import sys
import traceback
import re
from schemagic import validate_against_schema


def validate(schema, data):
    """Function that performs schema check validation."""
    try:
        print("\n\n")
        print(schema)
        print(data)
        print(validate_against_schema(schema, data))
        print("pass")
    except (ValueError, TypeError) as e:
        print(e)


def is_type(value, expected_type):
    """Predicate for type of given value."""
    actual_type = type(value)
    if actual_type is not expected_type:
        msg = "Expected type: {expected}, but the value has type {actual}".format(
            expected=expected_type, actual=actual_type)
        raise TypeError(msg)


def name_str(value):
    """Check if value represents a name."""
    if not re.fullmatch("[A-Z][a-z]+", value):
        msg = "Proper name expected, but got '{value}' instead".format(value=value)
        raise TypeError(msg)


def pos_int(value):
    """Predicate for positive integer values."""
    is_type(value, int)
    if value <= 0:
        msg = "Positive number expected, but got {value} instead".format(value=value)
        raise TypeError(msg)


user = {"name": name_str,
        "surname": name_str,
        "id": pos_int}

validate(user, {"name": "Eda",
                "surname": "Wasserfall",
                "id": 1})

validate(user, {"name": "eda",
                "surname": "Wasserfall",
                "id": 1})

validate(user, {"name": "E",
                "surname": "Wasserfall",
                "id": 1})

validate(user, {"name": "Eda",
                "id": 1})

validate(user, {"name": "Eda",
                "surname": "Wasserfall",
                "id": 0})
