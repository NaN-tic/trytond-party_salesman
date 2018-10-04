# This file is part of party_salesman module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import ModelSQL, fields
from trytond.pool import PoolMeta

__all__ = ['Employee', 'PartySalesman', 'Party']


class Employee(metaclass=PoolMeta):
    __name__ = 'company.employee'
    salesman = fields.Boolean('Salesman',
        help='If you check this field, this employee will be available as a '
                'salesman agent.')


class PartySalesman(ModelSQL):
    'Party - Salesman'
    __name__ = 'party.party-company.employee.salesman'
    party = fields.Many2One('party.party', 'Party', ondelete='CASCADE',
        select=True, required=True)
    salesman = fields.Many2One('company.employee', 'Salesman',
        ondelete='CASCADE', select=True, required=True)


class Party(metaclass=PoolMeta):
    __name__ = 'party.party'
    salesmans = fields.Many2Many('party.party-company.employee.salesman',
        'party', 'salesman', 'Salesmans', domain=[('salesman', '=', True)])
