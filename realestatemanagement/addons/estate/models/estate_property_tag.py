from odoo import models, fields
class EstatePropertyTag(models.Model):

    _name="property.tag"

    _description='property tags'
    _sql_constraints = [
        ('name', 'unique(name)', 'Property tag must be unique')
    ]
    name=fields.Char(required=True,string="Tags")

