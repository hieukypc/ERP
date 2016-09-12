'''
Created on Sep 12, 2016

@author: phcuong
'''

from openerp import models, fields#, api


# Use API v9. Define new class 
class mrp_routing_workcenter_input(models.Model):
    """
    Define porperty input for a workcenter.
    """
    _name = 'mrp.routing.workcenter.input'
    _description = 'Property data input of a work center'
    
    code = fields.Char('Code', required=True, help="The code that can used for work center.")
    name = fields.Char('Description', required=True)
    input_id = fields.Integer()
    
class mrp_routing_workcenter_ouput(models.Model):
    """
    Define porperty output for a workcenter.
    """
    _name = 'mrp.routing.workcenter.output'
    _description = 'Property data output of a work center'

    code = fields.Char('Code', required=True, help="The code that can used for work center.")
    name = fields.Char('Description', required=True)
    output_id = fields.Integer()
    
# End of define. 