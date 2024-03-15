{
    'name': 'Highland purchase Indent',
    'version': '14.0.1',
    'summary': 'Po Indent Customization',
    'description': """Po module customization""",
    'category': 'purchase',
    'author': 'Live digital marketing solutions pvt ltd',
    'website': 'https://www.ldtech.in/',
    'depends': ['stock', 'purchase', 'mail', 'hr', 'bz_partner_category', 'purchase_requisition'],
    'data': [
            'security/ir.models.access.csv',
            'security/indent_security.xml',
            'data/purchase_indent_data.xml',
            'data/mail_template.xml',
            'views/purchase_indent_views.xml',
            'views/purchase_views.xml',
            'views/stock_picking_views.xml',
            'views/purchase_requisition_view.xml',
            'wizard/reject_remarks_views.xml',
             ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}

