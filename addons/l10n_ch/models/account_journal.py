# -*- coding: utf-8 -*-
# Part of ecommerce. See LICENSE file for full copyright and licensing details.

from ecommerce import models, fields, api

from ecommerce.exceptions import ValidationError

from ecommerce.addons.base_iban.models.res_partner_bank import validate_iban
from ecommerce.addons.base.models.res_bank import sanitize_account_number


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    invoice_reference_model = fields.Selection(selection_add=[
        ('ch', 'Switzerland')
    ], ondelete={'ch': lambda recs: recs.write({'invoice_reference_model': 'ecommerce'})})

    def _process_reference_for_sale_order(self, order_reference):
        '''
        returns the order reference to be used for the payment respecting the ISR
        '''
        self.ensure_one()
        if self.invoice_reference_model == 'ch':
            # converting the sale order name into a unique number. Letters are converted to their base10 value
            invoice_ref = "".join([a if a.isdigit() else str(ord(a)) for a in order_reference])
            # id_number = self.company_id.bank_ids.l10n_ch_postal or ''
            order_reference = self.env['account.move']._compute_isr_number(invoice_ref)
            return order_reference
        return super()._process_reference_for_sale_order(order_reference)
