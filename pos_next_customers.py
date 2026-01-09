# -*- coding: utf-8 -*-
# Copyright (c) 2024, POS Next and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def auto_assign_loyalty_program(doc, method):
    """
    Automatically assign loyalty program to new customers.
    This is called after a new Customer is inserted.
    """
    try:
        # Get the default loyalty program if exists
        default_loyalty = frappe.db.get_single_value('Selling Settings', 'default_loyalty_program')
        
        if default_loyalty and not doc.loyalty_program:
            doc.db_set('loyalty_program', default_loyalty)
            frappe.db.commit()
    except Exception as e:
        # Log error but don't block customer creation
        frappe.log_error(frappe.get_traceback(), 'Auto Assign Loyalty Program Error')
