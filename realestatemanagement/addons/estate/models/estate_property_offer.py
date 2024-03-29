from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import UserError
class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description="Offers received on each properties"
    _sql_constraints = [
        ('check_offer_price', 'CHECK(price>0)', 'Offer price must be strictly positive')
    ]
    price=fields.Float(required=True, string="price")
    partner_id=fields.Many2one("res.partner",   string="partner_id")
    property_id=fields.Many2one("estate.property", string="property_id", store=True)
    status=fields.Selection(string="status", selection=[('accepted','Accepted'), ('refused', 'Refused')], copy=False)
    validity = fields.Integer()
    deadline=fields.Date(compute="_compute_deadline", inverse="_inverse_deadline")
    @api.depends("create_date", "validity", "deadline")
    def _compute_deadline(self):
        for record in self:
            if record.create_date:
                date_delta=record.create_date.date()
                record.deadline=date_delta + timedelta(days=record.validity)
            else:
                date_delta=datetime.today()
                record.deadline=date_delta+timedelta(days=record.validity)
    @api.depends("validity", "deadline", "creat_date")
    def _inverse_deadline(self):

        for record in self:
            if record.create_date:
                date_delta=record.create_date.date()
                record.validity=(record.deadline-date_delta).days
            else:
                date_delta=datetime.today()
                record.validity = (record.deadline - date_delta).days

    def refuse_offer(self):
        self.status="refused"
        return self.status

    def accept_offer(self):
        for record in self:
            all_offers=record.property_id.offer_ids
            accepted_offer=all_offers.filtered(lambda x: x.status =='accepted')
            if accepted_offer:
                raise UserError("An offer has already been accepted on this property.")
            else:
                record.status='accepted'
                # set the buyer and corresping price as selling price
                for record in self:
                    record.property_id.buyer_id=record.partner_id.id
                    record.property_id.selling_price=record.price

        return True