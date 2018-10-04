# This file is part of of party_salesman module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import party


def register():
    Pool.register(
        party.Employee,
        party.PartySalesman,
        party.Party,
        module='party_salesman', type_='model')
