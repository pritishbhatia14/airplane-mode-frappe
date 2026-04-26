// Copyright (c) 2026, pritish and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
    refresh: function(frm) {

        frm.add_custom_button("Assign Seat", function() {

            frappe.prompt(
                "Enter Seat Number",
                function(values) {
                    frm.set_value("seat", values.value);
                },
                "Assign Seat"
            );

        }, "Actions");

    }
});
