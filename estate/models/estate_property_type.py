from odoo import api, models, fields

class PropertyType(models.Model):
    # Model Property
    _name = "estate.property.type"
    _description = "Estate App Property Types"
    _order = 'sequence, name'

    
    # Fields
    name = fields.Char(required = True)
    property_ids = fields.One2many("estate.property", "property_type_id", string="Properties")
    sequence = fields.Integer('Sequence', default=1)
    
    offer_ids = fields.One2many("estate.property.offer", "property_type_id", string="Offers")
    offer_count = fields.Integer(compute="_compute_offer_count")
    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for type in self:
            type.offer_count = len(type.offer_ids)