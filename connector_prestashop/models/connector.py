# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models


class ConnectorPrestashopInstalled(models.AbstractModel):
    """Empty model used to know if the module is installed in the
    database.

    If the model is in the registry, the module is installed.
    """
    _name = 'connector_prestashop.installed'
