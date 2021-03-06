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

"""Usage of Schema class."""

from sys import argv
from schema import Schema, SchemaError


def validate(schema, data, verbose_mode=False):
    """Perform schema validation check."""
    try:
        print("\n\n")
        if verbose_mode:
            print(schema)
        print(data)
        schema.validate(data)
        print("pass")
    except SchemaError as e:
        print(e)


def positive_integer(value):
    """Validate if value represents a positive integer value."""
    return type(value) is int and value > 0


def salary(value):
    """Validate if salary has proper value."""
    return type(value) is float and value > 10000.0 and value < 99999.9


employee = Schema({"name": str,
                   "surname": str,
                   "id": positive_integer,
                   "salary": salary,
                   "position": str})


verbose_mode = "-v" in argv

validate(employee, {"name": "Eda",
                    "surname": "Wasserfall",
                    "id": 1,
                    "salary": 15000.0,
                    "position": "QA"},
         verbose_mode)

validate(employee, {"name": "Eda",
                    "surname": "Wasserfall",
                    "id": 1,
                    "salary": 15000,
                    "position": "QA"},
         verbose_mode)

validate(employee, {"name": "Eda",
                    "surname": "Wasserfall",
                    "id": 1,
                    "salary": -15000.0,
                    "position": "QA"},
         verbose_mode)

validate(employee, {"name": "Eda",
                    "surname": "Wasserfall",
                    "id": 1,
                    "salary": 1000000.0,
                    "position": "QA"},
         verbose_mode)

validate(employee, {"name": "Eda",
                    "surname": "Wasserfall",
                    "id": 1,
                    "salary": 15000.0,
                    "position": "QA"},
         verbose_mode)

validate(employee, {"name": "Eda",
                    "id": 1,
                    "salary": 100000000.0,
                    "position": "QA"},
         verbose_mode)

validate(employee, {"name": "Eda",
                    "surname": "Wasserfall",
                    "id": 1,
                    "salary": 45000.0,
                    "position": ""},
         verbose_mode)

validate(employee, {"name": "Eda",
                    "surname": "Wasserfall",
                    "id": 1,
                    "salary": 45000.0,
                    "position": "tovarnik"},
         verbose_mode)

validate(employee, {"name": "",
                    "surname": "",
                    "id": 1,
                    "salary": 25000.0,
                    "position": ""},
         verbose_mode)
