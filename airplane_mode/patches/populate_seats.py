import frappe
import random

def execute():
    tickets = frappe.get_all("Airplane Ticket", fields=["name"])

    for ticket in tickets:
        seat = str(random.randint(1, 99)) + random.choice(["A","B","C","D","E"])

        frappe.db.set_value("Airplane Ticket", ticket.name, "seat", seat)

    frappe.db.commit()
