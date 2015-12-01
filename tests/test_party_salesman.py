# This file is part of the party_salesman module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class PartySalesmanTestCase(ModuleTestCase):
    'Test Party Salesman module'
    module = 'party_salesman'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        PartySalesmanTestCase))
    return suite