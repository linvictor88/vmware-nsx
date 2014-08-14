# Copyright 2014 OpenStack Foundation
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

"""nuage_provider_networks

Revision ID: aae5706a396
Revises: 3b85b693a95f
Create Date: 2014-08-18 16:00:21.898795

"""

revision = 'aae5706a396'
down_revision = '3b85b693a95f'

from alembic import op
import sqlalchemy as sa


def upgrade(active_plugins=None, options=None):
    op.create_table(
        'nuage_provider_net_bindings',
        sa.Column('network_id', sa.String(length=36), nullable=False),
        sa.Column('network_type', sa.String(length=32), nullable=False),
        sa.Column('physical_network', sa.String(length=64), nullable=False),
        sa.Column('vlan_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['network_id'], ['networks.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('network_id')
    )


def downgrade(active_plugins=None, options=None):
    op.drop_table('nuage_provider_net_bindings')
