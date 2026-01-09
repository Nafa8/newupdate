import frappe

def set_item_description(doc, method):
    if doc.item_name:
        doc.description = doc.item_name

def update_existing_items():
    items = frappe.get_all('Item', fields=['name', 'item_name', 'description'])
    count = 0
    for i in items:
        if i.description != i.item_name:
            frappe.db.set_value('Item', i.name, 'description', i.item_name)
            count += 1
    frappe.db.commit()
    print(f"Updated {count} items.")
