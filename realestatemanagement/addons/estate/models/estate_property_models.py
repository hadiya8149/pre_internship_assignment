from odoo import fields, models, api
from datetime import date, timedelta
from odoo.exceptions import ValidationError, UserError

class EstateProperties(models.Model):
    _name="estate.property"
    _description ="Model for Real Estate Management"
    _sql_constraints = [('check_expected_price', 'CHECK(expected_price>0)',
                         'The expected price should be strictly positive'),
                        ('check_selling_price', 'CHECK(selling_price>0)', 'Selling price should be strictly positive.')

                        ]

    name = fields.Char(required=True, readonly=True)
    description = fields.Text(readonly=True)
    postcode=fields.Char(readonly=True)
    date_availability = fields.Date(default=lambda x: (date.today()+timedelta(days=90)), copy=False)

    expected_price= fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms= fields.Integer(default=2)
    living_area=fields.Integer(string="living_area")
    facades=fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean()
    garden_area=fields.Integer(string="garden_area",compute="_compute_garden_properties")
    garden_orientation = fields.Selection(string='Garden Orientation', selection =[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])
    state=fields.Selection(required=True, default="new", copy=False, string='Status', selection =[('new', 'New'), ('offer received', 'Offer received'), ('offer accepted', 'Offer accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')])
    active = fields.Boolean(default=True)
    total_area=fields.Integer(compute="_compute_total_area")

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:  # This loop might be unnecessary
            record.total_area = record.living_area + record.garden_area

    property_type_id=fields.Many2one("estate.property.type", string="Property Type")
    tag_ids=fields.Many2many("property.tag",relation="property_id", string="Tags")

    buyer_id=fields.Many2one("res.partner", string="Buyer", default=lambda self: self.env.user, copy=False)
    seller_id = fields.Many2one("res.partner", string="Seller",default=lambda self: self.env.user)

    offer_ids=fields.One2many("estate.property.offer", inverse_name="property_id", string="offer")
    best_price = fields.Float(compute="_compute_best_offer")
    @api.depends("offer_ids.price")
    def _compute_best_offer(self):
        for record in self:

            record.best_price=max(self.offer_ids.mapped('price')) if record.offer_ids else 0.0
    @api.depends("garden", "garden_orientation")
    def _compute_garden_properties(self):
        for record in self:
            if record.garden==True:
                record.garden_area = 10

                record.garden_orientation = "north"
            else:
                record.garden_area=0
                record.garden_orientation="south"
    def cancel_ad(self):
        # raise error if it is already sold
        for record in self:
            if record.state=='sold':
                raise UserError("Sold properties cannot be canceled.")
            record.state='canceled'
        return True
    def sold_ad(self):
        # raise error if it is already canceled
        for record in self:
            if record.state=='canceled':
                raise UserError("Canceled properties cannot be sold.")
            else:

                record.state='sold'


    @api.constrains('selling_price')
    def _check_selling_price(self):
        for record in self:
            if record.selling_price<(0.9*record.expected_price):
                raise ValidationError("The selling price can't be 90% lower than expected_price")
