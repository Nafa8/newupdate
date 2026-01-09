# -*- coding: utf-8 -*-
# API module for POS Next

import frappe

# Import API modules to make them accessible
from . import invoices
from . import items
from . import shifts
from . import pos_profile
# Note: customers module is loaded via hooks, not imported here to avoid circular imports
from . import offers
from . import promotions
from . import utilities

@frappe.whitelist(allow_guest=True)
def ping():
    """Simple ping endpoint for connectivity checks"""
    return "pong"
