# -*- coding: utf-8 -*-
from odoo import http
class MaterialController(http.Controller):

    @http.route('/inventory/material', auth='user', type='json')
    def material(self):  
        return {
            'html': request.env.ref('inventory.material')._render({
            })
        }

