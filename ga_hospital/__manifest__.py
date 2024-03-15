# -*- coding: utf-8 -*-
{
    'name' : 'Hospital Management',
    'version' : '1.0',
    'summary': 'Hospital Management Software',
    'sequence': -100,
    'description': """Hospital Management Software""",
    'category': 'Productivity',
    'website': 'https://www.odoomates.tech',
    'depends' : [
        'sale',
        'mail',
        'report_xlsx',
        'base',
        'product'
                 ],
    'data': [
        'security/ir.models.access.csv',
        'wizard/create_appointment_view.xml',
        'wizard/appointment_report_view.xml',
        'wizard/all_patient_report_view.xml',
        'views/patient.xml',
        'views/doctor.xml',
        'views/sale.xml',
        'views/my_module_data.xml',
        'views/kids_view.xml',
        'views/patient_gender_view.xml',
        'views/appointment.xml',
        'views/partner.xml',
        'report/patient_details_template.xml',
        'report/patient_card.xml',
        'report/appointment_details.xml',
        'report/all_patient_list.xml',
        'report/report.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
