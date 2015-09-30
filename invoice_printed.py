# -*- coding: utf-8 -*-
from openerp.osv import osv,fields
class invoice_printed(osv.osv):
    _inherit = "account.invoice"
    _columns = {
        'invoice_printed': fields.selection(
        	(
        		('old','Previous record to module installation'),
        		('','Not printed'),
        		('printed','Printed')
        	),
           'Print status'
        ),
    }
    _defaults ={
        'invoice_printed': ''
    }
invoice_printed()
