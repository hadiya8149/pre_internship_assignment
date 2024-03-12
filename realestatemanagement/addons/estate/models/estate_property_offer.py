from odoo import models, fields
from datetime import datetime, timedelta
class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description="Offers received on each properties"
    _sql_constraints = [
        ('check_offer_price', 'CHECK(price>0)', 'Offer price must be strictly positive')
    ]
    price=fields.Float(required=True, string="price")
    partner_id=fields.Many2one("res.partner",  string="partner_id")
    property_id=fields.Many2one("estate.property", string="property_id")
    status=fields.Selection(string="status", selection=[('accepted','Accepted'), ('refused', 'Refused')], copy=False)
    validity = fields.Integer()
    deadline=fields.Date(compute="_compute_deadline_date", inverse="_compute_validity")

    def _compute_deadline_date(self):
        for record in self:
            record.deadline=timedelta(record.create_date)+timedelta(validity)
    def _compute_validity(self):
        for record in self:
            record.validity=timedelta.days(timedelta(record.create_date)-timedelta(record.deadline))

    def refuse_offer(self):
        pass
    def accept_offer(self):
        pass