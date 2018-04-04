from schema import Schema, SchemaError


def validate(schema, data):
    try:
        print("\n\n")
        print(schema)
        print(data)
        schema.validate(data)
        print("pass")
    except SchemaError as e:
        print(e)


integer_list = Schema([int])
float_list = Schema([float])
string_list = Schema([str])

validate(integer_list, [1, 2, 3])
validate(integer_list, [1.1, 2.2, 3.3])
validate(integer_list, ["1", "2", "3"])

validate(float_list, [1, 2, 3])
validate(float_list, [1.1, 2.2, 3.3])
validate(float_list, ["1", "2", "3"])

validate(string_list, [1, 2, 3])
validate(string_list, [1.1, 2.2, 3.3])
validate(string_list, ["1", "2", "3"])
