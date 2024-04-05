// Copyright (c) 2024, vedika and contributors
// For license information, please see license.txt

frappe.ui.form.on("Student", {
    refresh(frm) {
        frm.add_custom_button(__('Add Detail'), function() {
            frappe.prompt([
                {
                    fieldname: 'first_name',
                    label: __('First Name'),
                    fieldtype: 'Data'
                },
                {
                    fieldname: 'last_name',
                    label: __('Last Name'),
                    fieldtype: 'Data'
                },
                {
                    fieldname: 'phone_number',
                    label: __('Phone Number'),
                    fieldtype: 'Phone'
                }
            ],
            function(values){
                var child_table = cur_frm.add_child('details');
                child_table.first_name = values.first_name;
                child_table.last_name = values.last_name;
                child_table.phone_number = values.phone_number;
                refresh_field('details');
                cur_frm.save();
            }, __('Add Detail'));
        });
    }

});










