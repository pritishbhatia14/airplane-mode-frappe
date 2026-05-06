import frappe

def get_context(context):
    context.shops = frappe.get_all("Airport Shop", fields=[ "shop_name","route"])
