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
from schemagic import validate_against_schema


def validate(schema, data):
    """Function that performs schema check validation."""
    try:
        print("\n\n")
        print(schema)
        print(data)
        print(validate_against_schema(schema, data))
        print("pass")
    except (ValueError, TypeError, AssertionError) as e:
        print(e)
        traceback.print_exc(file=sys.stdout)


def is_type(value, expected_type):
    """Predicate for type of given value."""
    assert type(value) is expected_type


def is_int(value):
    """Predicate for integer values."""
    is_type(value, int)


def is_float(value):
    is_type(value, float)


integer_list = [is_int]
float_list = [is_float]
string_list = [lambda x: is_type(x, str)]

validate(integer_list, [1, 2, 3])
validate(integer_list, ["hello", "world", "!"])
validate(integer_list, ["1", 1.5])

validate(float_list, [1, 2, 3])
validate(float_list, ["hello", "world", "!"])
validate(float_list, ["1", 1.5, "3.1415"])

validate(string_list, [1, 2, 3, 4])
validate(string_list, ["hello", "world", "!"])
