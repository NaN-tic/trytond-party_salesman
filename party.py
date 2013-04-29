# This file is part of party_salesman module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import ModelSQL, fields
from trytond.pool import Pool, PoolMeta
from trytond.pyson import Eval, Bool

__all__ = [
    'PartySalesman',
    'Party',
]
__metaclass__ = PoolMeta


class PartySalesman(ModelSQL):
    'Party - Salesmans'
    __name__ = 'party.party-sale.salesman'
    party = fields.Many2One('party.party', 'Party', ondelete='CASCADE',
        select=True, required=True)
    salesman = fields.Many2One('party.party', 'Salesman', ondelete='CASCADE',
        select=True, required=True)


class Party():
    __name__ = 'party.party'
    agent = fields.Boolean('Agent',
        help='If you check this field, this party will be available as a '
                'creditor or agent.')
    salesmans = fields.Many2Many('party.party-sale.salesman',
        'salesman', 'party', 'Salesmans',
        )
