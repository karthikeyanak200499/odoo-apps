{
    "name": "Employee Exit Interview Form",
    "version": "1.0",
    "depends": ["base", "hr", "mail"],
    "author": "Karthikeyan A",
    "category": "Human Resources",
    "description": "Custom module for Employee Exit Interview Form",
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/employee_exit_form.xml"
    ],
    'images': ['static/description/banner.png'],
    "installable": True,
    "application": True,
}
