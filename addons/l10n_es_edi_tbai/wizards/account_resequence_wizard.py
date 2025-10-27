# Part of ecommerce. See LICENSE file for full copyright and licensing details.
from ecommerce import models


class AccountResequenceWizard(models.TransientModel):
    _inherit = "account.resequence.wizard"

    def _frozen_edi_documents(self):
        docs = super()._frozen_edi_documents()
        # TicketBAI/Batuz vendor bills are sent with ref, so they can be resequenced
        return docs.filtered(
            lambda doc: doc.edi_format_id.code != "es_tbai"
            or doc.move_id.is_sale_document()
        )
