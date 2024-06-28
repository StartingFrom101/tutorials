from odoo import models, Command

class estate_property(models.Model):
    _inherit = 'estate.property'
    
    def property_action_sold(self):
        for property in self:    
            journal = self.env["account.journal"].search([("type", "=", "sale")], limit=1)            
            # to create an object, use self.env[model_name].create(values),  where values is a dict
            self.env['account.move'].create({
                'partner_id' : property.buyer_id.id,
                'move_type' : 'out_invoice',
                'journal_id' : journal.id,
                'invoice_line_ids' : [
                    Command.create({ 
                        'name' : property.name,
                        'price_unit' : property.selling_price * 1.06,
                        'quantity' : 1 }),
                    Command.create({ 
                        'name' : "Admin Fees",
                        'price_unit' : 100,
                        'quantity' : 1 })
                ],
            })
        
        return super().property_action_sold()
    
    