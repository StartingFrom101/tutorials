from odoo import models, fields

class PropertyTag(models.Model):
    # Model Property
    _name = 'estate.property.tag'
    _description = 'Estate property tags'
    _order = 'name'
    
    # Fields
    name = fields.Char(required=True)
    color = fields.Integer()
