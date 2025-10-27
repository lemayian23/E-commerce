# -*- coding: utf-8 -*-
from ecommerce import models
from ecommerce.tools.translate import _
from ecommerce.exceptions import UserError


class AccountMoveReversal(models.TransientModel):
    _inherit = 'account.move.reversal'

    def reverse_moves(self):
        self.ensure_one()
        for move in self.move_ids:
            if move.journal_id.country_code == 'SA' and not self.reason:
                raise UserError(_("For Credit/Debit notes issued in Saudi Arabia, you need to specify a Reason"))
        return super().reverse_moves()
