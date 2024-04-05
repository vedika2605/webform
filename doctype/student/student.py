# Copyright (c) 2024, vedika and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document
# class Student(Document):
	
# 	def update_demo_from_details(doc, method):
# 		if method == "on_update" and doc.doctype == "Student" and doc.details:
# 			for detail in doc.details:
# 				if detail.phone_number:
# 					demo_record = frappe.db.exists({
# 						"doctype": "Demo",
# 						"parent": doc.name,
# 						"parentfield": "demo",
# 						"parenttype": "Student",
# 						"first_name": detail.first_name,
# 						"last_name": detail.last_name
# 						})
# 				if not demo_record:

#                     demo = frappe.get_doc({
#                         "doctype": "Demo",
#                         "parent": doc.name,
#                         "parentfield": "demo",
#                         "parenttype": "Student",
#                         "first_name": detail.first_name,
#                         "last_name": detail.last_name,
#                         "phone_number": detail.phone_number
#                     })
#                     demo.insert(ignore_permissions=True)
#                 else:
#                     frappe.db.set_value("Demo", demo_record, "phone_number", detail.phone_number)


	# pass
import frappe
from frappe.model.document import Document

class Student(Document):

    def update_demo_from_details(doc, method):
        if method == "on_update" and doc.doctype == "Student" and doc.details:
            for detail in doc.details:
                if detail.phone_number:
                    demo_record = frappe.db.exists({
                        "doctype": "Demo",
                        "parent": doc.name,
                        "parentfield": "demo",
                        "parenttype": "Student",
                        "first_name": detail.first_name,
                        "last_name": detail.last_name
                    })
                    if not demo_record:
                        demo = frappe.get_doc({
                            "doctype": "Demo",
                            "parent": doc.name,
                            "parentfield": "demo",
                            "parenttype": "Student",
                            "first_name": detail.first_name,
                            "last_name": detail.last_name,
                            "phone_number": detail.phone_number
                        })
                        demo.insert(ignore_permissions=True)
                    else:
                        frappe.db.set_value("Demo", demo_record, "phone_number", detail.phone_number)

