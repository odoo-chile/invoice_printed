# -*- coding: utf-8 -*-
from openerp import models, fields

class invoice_printed(models.Model):
    
    _inherit = "account.invoice"
    
    invoice_printed = fields.Selection((
        ('old','Previous record to module installation'), ('','Not printed'),
        ('printed','Printed')), 'Print status', default='')

    controller_cmnd = fields.Text('Fiscal Controller Print Command')

    controller_ansr = fields.Text('Fiscal Controller Answer')
