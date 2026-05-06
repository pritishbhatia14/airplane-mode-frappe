# Copyright (c) 2026, pritish and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document

class AirplaneFlight(WebsiteGenerator):
    def on_submit(self):
        self.status = "Completed"
    def before_save(self):
        if not self.route:
            self.route = (f"flights/{self.name}")

