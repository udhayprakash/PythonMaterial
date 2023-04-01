from pprint import pp

from marshmallow import Schema, fields


class CategorySchema(Schema):
    id = fields.Integer()
    name = fields.String()


class ProductSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    price = fields.Float()
    category = fields.Nested(CategorySchema)


# Example usage
category_data = {"id": 1, "name": "Clothing"}
product_data = {"id": 1, "name": "T-Shirt", "price": 19.99, "category": category_data}

# Load the data into the schema
loaded_data = ProductSchema().load(product_data)

# Dump the data back out of the schema
dumped_data = ProductSchema().dump(loaded_data)

pp(dumped_data)
