# -*- coding: utf-8 -*-
# Part of ecommerce. See LICENSE file for full copyright and licensing details.

from ecommerce import models, _


class MailBot(models.AbstractModel):
    _inherit = 'mail.bot'

    def _get_answer(self, record, body, values, command):
        ecommercebot_state = self.env.user.ecommercebot_state
        if self._is_bot_in_private_channel(record):
            if ecommercebot_state == "onboarding_attachement" and values.get("attachment_ids"):
                self.env.user.ecommercebot_failed = False
                self.env.user.ecommercebot_state = "onboarding_canned"
                return _("Wonderful! 😇<br/>Try typing <span class=\"o_ecommercebot_command\">:</span> to use canned responses.")
            elif ecommercebot_state == "onboarding_canned" and self.env.context.get("canned_response_ids"):
                self.env.user.ecommercebot_failed = False
                self.env.user.ecommercebot_state = "idle"
                return _("Good, you can customize canned responses in the live chat application.<br/><br/><b>It's the end of this overview</b>, you can now <b>close this conversation</b> or start the tour again with typing <span class=\"o_ecommercebot_command\">start the tour</span>. Enjoy discovering ecommerce!")
            # repeat question if needed
            elif ecommercebot_state == 'onboarding_canned' and not self._is_help_requested(body):
                self.env.user.ecommercebot_failed = True
                return _("Not sure what you are doing. Please, type <span class=\"o_ecommercebot_command\">:</span> and wait for the propositions. Select one of them and press enter.")
        return super(MailBot, self)._get_answer(record, body, values, command)
