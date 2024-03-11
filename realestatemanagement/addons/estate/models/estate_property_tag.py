from odoo import models, fields
class EstatePropertyTag(models.Model):
    _name="property.tag"
    _description='property tags'
    name=fields.Char(required=True, string="Tags")
