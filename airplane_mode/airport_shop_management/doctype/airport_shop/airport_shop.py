
import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirportShop(WebsiteGenerator):
    def before_insert(self):
        settings = frappe.get_single("Shop Settings")

        if self.rent_amount in (None, 0):
            self.rent_amount = settings.default_rent_amount

    def after_insert(self):
        update_shop_counts(self.airport)

    def on_update(self):
        update_shop_counts(self.airport)

    def on_trash(self):
        update_shop_counts(self.airport)

    def before_save(self):
        if not self.route:
            self.route = f"shops/{self.name}"


def update_shop_counts(airport):
    shops = frappe.get_all("Airport Shop", filters={"airport": airport}, fields=["status"])

    total = len(shops)
    occupied = len([s for s in shops if s.status == "Occupied"])

    frappe.db.set_value(
        "Airport",
        airport,
        {"total_shops": total, "occupied_shops": occupied, "available_shops": total - occupied},
        )
