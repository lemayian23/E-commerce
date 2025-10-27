# Part of ecommerce. See LICENSE file for full copyright and licensing details.

from ecommerce import models


class IrHttp(models.AbstractModel):
    _inherit = ["ir.http"]

    @classmethod
    def _get_translation_frontend_modules_name(cls):
        modules = super()._get_translation_frontend_modules_name()
        return modules + ["survey"]
