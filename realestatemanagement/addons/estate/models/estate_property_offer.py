from odoo import models, fields, api
from datetime import datetime, timedelta
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
    validity = fields.Integer(default=7)
    deadline=fields.Date(default=datetime.today()+timedelta(7),compute="_compute_deadline", inverse="_inverse_deadline")
    @api.depends("create_date", "validity")
    def _compute_deadline(self):
        for record in self:
            if record.deadline:
                print(imedelta.days(timedelta(record.create_date.date())-timedelta(record.deadline)))

                record.deadline=timedelta(record.create_date.date())+timedelta(validity)

    def _inverse_deadline(self):
        for record in self:
            if record.create_date:

                record.validity=timedelta.days(timedelta(record.create_date.date())-timedelta(record.deadline))
            else:
                record.validity=timedelta.days(timedelta(datetime.today())-timedelta(record.deadline))

    def refuse_offer(self):
        self.status="refused"
        return self.status

    def accept_offer(self):
        # if the offer is accepted set the status to accepted.
        # if the offer is already accepted then state an offer has already been accepted
        # just simply change the active to false
        pass