# Copyright (c) 2024, vedika and contributors
# For license information, please see license.txt
import frappe

def execute(filters=None):
    columns = [
        {"label": "Sales Order", "fieldname": "sales_order", "fieldtype": "Link", "options": "Sales Order"},
        {"label": "Item Code", "fieldname": "item_code", "fieldtype": "Link", "options": "Item"},
        {"label": "Item Name", "fieldname": "item_name", "fieldtype": "Data"},
        {"label": "Quantity Ordered", "fieldname": "qty_ordered", "fieldtype": "Float"},
        {"label": "Rate", "fieldname": "rate", "fieldtype": "Currency"},
        {"label": "Total Amount", "fieldname": "total_amount", "fieldtype": "Currency"},
        {"label": "Sales Invoice", "fieldname": "sales_invoice", "fieldtype": "Link", "options": "Sales Invoice"}
    ]

    data = []
    
    sql_query = """
        SELECT 
            so.name AS sales_order, 
            sod.item_code, 
            sod.item_name, 
            sod.qty, 
            sod.rate, 
            sod.amount AS total_amount, 
            si.name AS sales_invoice
        FROM 
            `tabSales Order` so 
        INNER JOIN 
            `tabSales Order Item` sod ON so.name = sod.parent
        LEFT JOIN 
            `tabSales Invoice Item` sii ON sod.item_code = sii.item_code
        LEFT JOIN 
            `tabSales Invoice` si ON sii.parent = si.name
        WHERE 
            so.docstatus = 1
            {conditions}
        ORDER BY 
            so.name
    """

    conditions = ""
    if filters.get("from_date"):
        conditions += " AND so.transaction_date >= '{}'".format(filters.get("from_date"))
    if filters.get("to_date"):
        conditions += " AND so.transaction_date <= '{}'".format(filters.get("to_date"))

    sql_query = sql_query.format(conditions=conditions)
    sales_order_items = frappe.db.sql(sql_query, as_dict=True)
    for row in sales_order_items:
        data.append(row)
    return columns, data
