# -*- coding: utf-8 -*-
from openerp.osv import osv,fields
class picking_printed(osv.osv):
    _inherit = "stock.picking"
    _columns = {
        'picking_printed': fields.selection(
        	(
        		('old','Previous record to module installation'),
        		('','Not printed'),
        		('printed','Printed')
        	),
           'Print status'
        ),
    }
    _defaults ={
        'picking_printed': ''
    }
picking_printed()
