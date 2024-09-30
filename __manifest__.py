
{
    'name': 'Stock Request Order Report',
    'version': '1.0',
    'summary': 'Print Stock Request Order',
    'description': 'Module to print Stock Request Order with detailed information.',
    'category': 'Inventory',
    'author': 'Your Name',
    'depends': ['stock', 'stock_request'],
    'data': [
        'views/stock_request_order_view.xml',
        'report/stock_request_order_report.xml',
        'report/stock_request_order_template.xml',
    ],
    'installable': True,
    'application': False,
}
