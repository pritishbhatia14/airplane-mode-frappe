import frappe

def send_rent_reminders():
    settings = frappe.get_doc("Airport Shop Settings")

    if not settings.enable_rent_reminder:
        return

    tenants = frappe.get_all("Tenant", fields=["name", "email"])

    for t in tenants:
        frappe.sendmail(
            recipients=t.email,
            subject="Rent Due Reminder",
            message="Your rent is due this month."
        )
