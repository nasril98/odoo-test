# -*- coding: utf-8 -*-
from odoo import api, fields, models

class InventorySupplier(models.Model):
    _name = "inventory.supplier"
    _description = "Supplier Data"
    code = fields.Char(string='supplier code', required=True, translate=True)
    description = fields.Char(string='supplier description', required=True, translate=True)

class InventoryMaterial(models.Model):
    _name = "inventory.material"
    _description = "Material Data"
    code = fields.Char(string='Material Code', required=True, translate=True)
    description = fields.Char(string='Material Name', required=True, translate=True)
    material_type = fields.Selection([
        ('fabric','Fabric'),
        ('jeans','Jeans'),
        ('cotton','Cotton'),
    ])
    material_buy_price = fields.Integer(string='Material Buy Price',max=100, required=True, translate=True)
    related_supplier_id = fields.Many2one('inventory.supplier',related='inventory.supplier.code', string='Supplier',required=True)
