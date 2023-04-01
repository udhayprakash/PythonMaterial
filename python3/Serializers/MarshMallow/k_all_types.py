from enum import Enum

from marshmallow import Schema, fields, validate


class ExampleEnum(Enum):
    VALUE1 = "value1"
    VALUE2 = "value2"


class MyExampleSchema(Schema):
    my_field = fields.Field()
    my_raw = fields.Raw()
    my_nested = fields.Nested(lambda: MyExampleSchema())
    my_mapping = fields.Mapping(keys=fields.String(), values=fields.Integer())
    my_dict = fields.Dict(keys=fields.String(), values=fields.String())
    my_list = fields.List(fields.String())
    my_tuple = fields.Tuple(fields.Integer(), fields.Integer())
    my_string = fields.String(validate=validate.Length(max=50))
    my_uuid = fields.UUID()
    my_number = fields.Number()
    my_integer = fields.Integer()
    my_decimal = fields.Decimal()
    my_boolean = fields.Boolean()
    my_float = fields.Float()
    my_datetime = fields.DateTime()
    my_naive_datetime = fields.NaiveDateTime()
    my_aware_datetime = fields.AwareDateTime()
    my_time = fields.Time()
    my_date = fields.Date()
    my_timedelta = fields.TimeDelta()
    my_url = fields.Url()
    my_URL = fields.URL()
    my_email = fields.Email()
    my_ip = fields.IP()
    my_ipv4 = fields.IPv4()
    my_ipv6 = fields.IPv6()
    my_ip_interface = fields.IPInterface()
    my_ipv4_interface = fields.IPv4Interface()
    my_ipv6_interface = fields.IPv6Interface()
    my_enum = fields.Enum(ExampleEnum)
    my_method = fields.Method("get_method_value")
    my_function = fields.Function(lambda obj: obj.my_field.upper())
    my_str = fields.Str()
    my_bool = fields.Bool()
    my_int = fields.Int()
    my_constant = fields.Constant("some constant value")
    my_pluck = fields.Pluck("MyOtherSchema", "some_field_name")

    def get_method_value(self, obj):
        return obj.my_field.lower()
