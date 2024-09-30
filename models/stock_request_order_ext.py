
from odoo import models

class StockRequestOrder(models.Model):
    _inherit = 'stock.request.order'

    def action_print_stock_request(self):
        return self.env.ref('custom_module_stock_request_report.stock_request_order_report_action').report_action(self)
