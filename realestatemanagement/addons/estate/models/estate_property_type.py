from odoo import models, fields


class EstatePropertyTypes(models.Model):
    _name="estate.property.type"
    _description = "Type of property"
    name=fields.Char(required=True)