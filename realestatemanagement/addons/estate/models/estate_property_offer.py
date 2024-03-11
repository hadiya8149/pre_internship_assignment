from odoo import models, fields
class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description="Offers received on each properties"
    price=fields.Float(required=True, string="price")
    partner_id=fields.Many2one("res.partner",  string="partner_id")
    property_id=fields.Many2one("estate.property", string="property_id")
    status=fields.Selection(string="status", selection=[('accepted','Accepted'), ('refused', 'Refused')], copy=False)
