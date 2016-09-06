from openerp.osv import fields, osv

class daily_transation(osv.osv):
    _name = "daily.transaction"
    _description = "Daily Transaction"
    
    _columns = {
        'subject': fields.char('Subject', size=128, require=True),
        'date': fields.date('Date', require=True),
        'note': fields.text('Notes'),
        'amount': fields.float('Amount', require=True),
        'type': fields.selection([
            ('transport', 'Transport'),
            ('household', 'Household'),
            ('personal', 'Personal'),
            ], 'Type', requrie=True),
               
    }
