import frappe
from frappe.model.document import Document


class AirplaneTicket(Document):

    def validate(self):
        self.check_capacity()
        self.remove_duplicate_addons()
        self.calculate_total()

    def before_submit(self):
        self.validate_boarding_status()

    def calculate_total(self):
        total = self.flight_price or 0

        for row in self.add_ons:
            total += row.amount or 0

        self.total_amount = total

    def remove_duplicate_addons(self):
        items = []
        unique_rows = []

        for row in self.add_ons:
            if row.item not in items:
                items.append(row.item)
                unique_rows.append(row)

        self.set("add_ons", unique_rows)

    def validate_boarding_status(self):
        if self.status != "Boarded":
            frappe.throw("Ticket can only be submitted when status is Boarded")

    def check_capacity(self):
        airplane = frappe.db.get_value(
            "Airplane Flight",
            self.flight,
            "airplane"
        )

        capacity = frappe.db.get_value(
            "Airplane",
            airplane,
            "capacity"
        )

        booked_tickets = frappe.db.count(
            "Airplane Ticket",
            {"flight": self.flight}
        )

        if booked_tickets >= capacity and self.is_new():
            frappe.throw("Flight is full")
