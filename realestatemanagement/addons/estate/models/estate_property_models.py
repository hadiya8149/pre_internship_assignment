from odoo import fields, models, api
from datetime import date, timedelta
# import env
class EstateProperties(models.Model):

    _name="estate.property"
    _description ="Model for Real Estate Management"
    name = fields.Char(required=True, readonly=True)
    description = fields.Text(readonly=True)
    postcode=fields.Char(readonly=True)
    date_availability = fields.Date(default=lambda x: (date.today()+timedelta(days=90)), copy=False)

    expected_price= fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms= fields.Integer(default=2)
    living_area=fields.Integer()
    facades=fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean()
    garden_area=fields.Integer()
    garden_orientation = fields.Selection(string='Garden Orientation', selection =[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])
    state=fields.Selection(required=True, default="new", copy=False, string='Status', selection =[('new', 'New'), ('offer received', 'Offer received'), ('offer accepted', 'Offer accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')])
    active = fields.Boolean()

    property_type_id=fields.Many2one("estate.property.type", string="Property type")
    tag_ids=fields.Many2many("property.tag", "name", string="Tags")


    buyer_id=fields.Many2one("res.partner", string="Buyer", default=lambda self: self.env.user, copy=False)
    seller_id = fields.Many2one("res.partner", string="Seller",default=lambda self: self.env.user)
    offer_ids=fields.One2many("estate.property.offer", inverse_name="partner_id", string="offer")
