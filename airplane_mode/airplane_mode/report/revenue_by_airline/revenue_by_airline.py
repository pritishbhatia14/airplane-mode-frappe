import frappe

def execute(filters=None):
    data = []
    total_revenue = 0

    airlines = frappe.get_all("Airline", fields=["name"])

    for airline in airlines:
        revenue = frappe.db.sql("""
            SELECT SUM(ticket.total_amount)
            FROM `tabAirplane Ticket` ticket
            JOIN `tabAirplane Flight` flight
                ON ticket.flight = flight.name
            JOIN `tabAirplane` airplane
                ON flight.airplane = airplane.name
            WHERE airplane.airline = %s
            AND ticket.docstatus = 1
        """, (airline.name,))[0][0] or 0

        total_revenue += revenue

        data.append({
            "airline": airline.name,
            "revenue": revenue
        })

    columns = [
        {"label": "Airline", "fieldname": "airline", "fieldtype": "Link", "options": "Airline"},
        {"label": "Revenue", "fieldname": "revenue", "fieldtype": "Currency"}
    ]

    chart = {
        "data": {
            "labels": [d["airline"] for d in data],
            "datasets": [{"values": [d["revenue"] for d in data]}]
        },
        "type": "donut"
    }

    summary = [{
        "value": total_revenue,
        "label": "Total Revenue",
        "datatype": "Currency"
    }]

    return columns, data, None, chart, summary
