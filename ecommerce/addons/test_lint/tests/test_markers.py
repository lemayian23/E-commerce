# -*- coding: utf-8 -*-
# Part of ecommerce. See LICENSE file for full copyright and licensing details.

import logging
import os
import ecommerce

from . import lint_case

_logger = logging.getLogger(__name__)
MARKERS = [b'<' * 7, b'>' * 7]
EXTENSIONS = ('.py', '.js', '.xml', '.less', '.sass')


class TestConflictMarkers(lint_case.LintCase):

    def check_file(self, fullpath_name):

        with open(fullpath_name, 'rb') as f:
            content = f.read()
            self.assertFalse(any(m in content for m in MARKERS), 'Conflict markers found in %s' % fullpath_name)

    def test_conflict_markers(self):
        """ Test that there are no conflict markers left in ecommerce files """

        counter = 0

        ecommerce_path = os.path.abspath(os.path.dirname(ecommerce.__file__))
        paths = ecommerce.addons.__path__ + [ecommerce_path]
        paths.remove(os.path.join(ecommerce_path, 'addons'))  # avoid checking ecommerce/addons twice

        for p in paths:
            for dp, _, file_names in os.walk(p):
                if 'node_modules' in dp:
                    continue
                for fn in file_names:
                    if fn.endswith(EXTENSIONS):
                        self.check_file(os.path.join(dp, fn))
                        counter += 1
        _logger.info('%s files tested', counter)
