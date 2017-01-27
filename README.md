INVOICE PRINTED - ODOO
===========================
Este modulo crea un campo "invoice_printed" en account.invoice, que permite conocer
el estado de impresión del documento.

Notas de la Versión 0.2: 

Si se instala sobre una instancia en uso, para evitar que inicie la impresión de todas las facturas ya emitidas, deberá ejecutar la siguiente query a la base de datos a continuación de instalar el módulo:

update account_invoice set invoice_printed = 'old' where type = 'out_invoice'
    
Este módulo debe usarse en conjunto con el agente de impresión "prnfiscal"


