import frappe
from frappe.model.document import Document
import random


class AirplaneTicket(Document):

    def before_insert(self):
        self.assign_random_seat()

    def validate(self):
        self.remove_duplicate_addons()
        self.calculate_total()

    def before_submit(self):
        self.validate_boarding_status()

    def assign_random_seat(self):
        number = random.randint(1, 99)
        letter = random.choice(["A", "B", "C", "D", "E"])
        self.seat = f"{number}{letter}"

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
