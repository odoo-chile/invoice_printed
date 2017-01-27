# -*- coding: utf-8 -*-
from openerp import models, fields


class picking_printed(models.Model):
    
    _inherit = "stock.picking"
    
    picking_printed = fields.Selection((
        ('old','Previous record to module installation'), ('','Not printed'),
    	('printed','Printed')), 'Print status', default='')
