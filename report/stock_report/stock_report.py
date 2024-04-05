# Copyright (c) 2024, vedika and contributors
# For license information, please see license.txt

# import frappe

def execute(filters=None):
    columns = [
        {
            "fieldname": "customer_name",
            "label": "Customer Name",
            "fieldtype": "data",
            "width": 150
        },
		{
			"fieldname":"order_type",
			"label":"order type",
			"fieldtype":"select",
			"width":200

		}
    ]
    data = [
        {"customer_name": "Aditi","order_type":"sales"},
        {"customer_name": "Rani","order_type":"sales"},
		{"customer_name": "Kirti","order_type":"sales"},
		{"customer_name": "Tarun","order_type":"sales"},
		{"customer_name": "Tanvi","order_type":"sales"}
    ]



    return columns, data

