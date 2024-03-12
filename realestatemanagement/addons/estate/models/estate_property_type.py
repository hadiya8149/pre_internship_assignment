from odoo import models, fields

class EstatePropertyTypes(models.Model):
    _name="estate.property.type"
    _description = "Type of property"
    _sql_constraints=[
        ('unique_name', 'unique(name)', 'Property type must be unique')
    ]

    name=fields.Char(required=True, string="Property Type")
