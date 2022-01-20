# -*- coding: utf-8 -*-


@tagged('post_install', '-at_install')
class TestMaterial(Material):

    def test_material(self):

        self.env['material.add'].create({
            'code': 'entry',
            'description': 'Test Desc',
            'material_type': 'cotton',
            'material_buy_price': 50,
            'related_supplier_id': '1'
        })
