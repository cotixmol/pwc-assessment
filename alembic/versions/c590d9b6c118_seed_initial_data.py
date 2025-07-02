"""Seed Initial Data

Revision ID: c590d9b6c118
Revises: b5e5337cd866
Create Date: 2025-07-02 04:14:23.864730

"""
from typing import Sequence, Union
import datetime
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'c590d9b6c118'
down_revision: Union[str, Sequence[str], None] = 'b5e5337cd866'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Populate the database with initial seed data."""
    producers_table = sa.table('producers',
        sa.column('id', sa.Integer),
        sa.column('name', sa.String),
        sa.column('email', sa.String)
    )
    crops_table = sa.table('crops',
        sa.column('id', sa.Integer),
        sa.column('type', sa.String),
        sa.column('brand', sa.String)
    )
    harvests_table = sa.table('harvests',
        sa.column('id', sa.Integer),
        sa.column('producer_id', sa.Integer),
        sa.column('crop_id', sa.Integer),
        sa.column('harvest_date', sa.Date),
        sa.column('quantity_tonnes', sa.Float)
    )
    sales_table = sa.table('sales',
        sa.column('id', sa.Integer),
        sa.column('harvest_id', sa.Integer),
        sa.column('sale_date', sa.Date),
        sa.column('quantity_sold', sa.Float),
        sa.column('price_per_tonne', sa.Float)
    )

    op.bulk_insert(producers_table, [
        {'id': 1, 'name': 'Estancia Don Alberto S.A.', 'email': 'contacto@don-alberto.com.ar'},
        {'id': 2, 'name': 'Agropecuaria Los Girasoles SRL', 'email': 'info@losgirasoles.com'},
        {'id': 3, 'name': 'Familia Rossi Agro', 'email': 'rossi.agro@gmail.com'},
        {'id': 4, 'name': 'Campos del Litoral S.A.', 'email': 'admin@camposlitoral.com.ar'},
        {'id': 5, 'name': 'El Cencerro S.R.L.', 'email': 'elcencerro@outlook.com'},
        {'id': 6, 'name': 'La Pampa Verde Corp', 'email': 'compras@lpverde.com'},
        {'id': 7, 'name': 'Agro-Ganadera Del Sur', 'email': 'ags@gmail.com'},
    ])

    op.bulk_insert(crops_table, [
        {'id': 1, 'type': 'SOYBEAN', 'brand': 'DonMario 46R12'},
        {'id': 2, 'type': 'SOYBEAN', 'brand': 'Nidera A 5009 RG'},
        {'id': 3, 'type': 'WHEAT', 'brand': 'Baguette 620'},
        {'id': 4, 'type': 'WHEAT', 'brand': 'Klein Rayo'},
        {'id': 5, 'type': 'SUNFLOWER', 'brand': 'Advanta 860 CL'},
        {'id': 6, 'type': 'SUNFLOWER', 'brand': 'Nuseed Condor'},
        {'id': 7, 'type': 'CORN', 'brand': 'LG Dekalb 7210'},
        {'id': 8, 'type': 'CORN', 'brand': 'Breavant 2121'},
        {'id': 9, 'type': 'SORGHUM', 'brand': 'Advanta ADV5220'},
    ])

    op.bulk_insert(harvests_table, [
        {'id': 1, 'producer_id': 1, 'crop_id': 1, 'harvest_date': datetime.date(2024, 4, 15), 'quantity_tonnes': 2500.50},
        {'id': 2, 'producer_id': 1, 'crop_id': 7, 'harvest_date': datetime.date(2024, 3, 20), 'quantity_tonnes': 3200.00},
        {'id': 3, 'producer_id': 2, 'crop_id': 5, 'harvest_date': datetime.date(2024, 2, 25), 'quantity_tonnes': 1800.75},
        {'id': 4, 'producer_id': 2, 'crop_id': 3, 'harvest_date': datetime.date(2024, 11, 30), 'quantity_tonnes': 4100.20},
        {'id': 5, 'producer_id': 3, 'crop_id': 2, 'harvest_date': datetime.date(2024, 5, 2), 'quantity_tonnes': 1550.00},
        {'id': 10, 'producer_id': 3, 'crop_id': 4, 'harvest_date': datetime.date(2024, 12, 5), 'quantity_tonnes': 2200.00},
        {'id': 6, 'producer_id': 4, 'crop_id': 9, 'harvest_date': datetime.date(2024, 3, 10), 'quantity_tonnes': 950.50},
        {'id': 9, 'producer_id': 4, 'crop_id': 8, 'harvest_date': datetime.date(2025, 3, 28), 'quantity_tonnes': 5300.00},
        {'id': 7, 'producer_id': 5, 'crop_id': 1, 'harvest_date': datetime.date(2025, 4, 22), 'quantity_tonnes': 780.00},
        {'id': 8, 'producer_id': 5, 'crop_id': 6, 'harvest_date': datetime.date(2025, 2, 18), 'quantity_tonnes': 1100.50},
        {'id': 11, 'producer_id': 6, 'crop_id': 4, 'harvest_date': datetime.date(2025, 1, 10), 'quantity_tonnes': 8500.00},
        {'id': 12, 'producer_id': 6, 'crop_id': 2, 'harvest_date': datetime.date(2025, 5, 5), 'quantity_tonnes': 12000.00},
        {'id': 13, 'producer_id': 7, 'crop_id': 7, 'harvest_date': datetime.date(2025, 4, 1), 'quantity_tonnes': 4500.00},
    ])

    op.bulk_insert(sales_table, [
        {'id': 1, 'harvest_id': 1, 'sale_date': datetime.date(2024, 4, 25), 'quantity_sold': 1000.0, 'price_per_tonne': 285.50},
        {'id': 2, 'harvest_id': 1, 'sale_date': datetime.date(2024, 5, 10), 'quantity_sold': 1500.5, 'price_per_tonne': 290.00},
        {'id': 3, 'harvest_id': 2, 'sale_date': datetime.date(2024, 4, 1), 'quantity_sold': 3000.0, 'price_per_tonne': 175.20},
        {'id': 4, 'harvest_id': 3, 'sale_date': datetime.date(2024, 3, 5), 'quantity_sold': 1800.75, 'price_per_tonne': 350.80},
        {'id': 5, 'harvest_id': 4, 'sale_date': datetime.date(2024, 12, 15), 'quantity_sold': 2000.0, 'price_per_tonne': 220.00},
        {'id': 11, 'harvest_id': 4, 'sale_date': datetime.date(2024, 12, 20), 'quantity_sold': 2100.2, 'price_per_tonne': 225.50},
        {'id': 6, 'harvest_id': 5, 'sale_date': datetime.date(2024, 5, 20), 'quantity_sold': 1550.0, 'price_per_tonne': 288.75},
        {'id': 7, 'harvest_id': 7, 'sale_date': datetime.date(2025, 5, 1), 'quantity_sold': 780.0, 'price_per_tonne': 295.00},
        {'id': 8, 'harvest_id': 8, 'sale_date': datetime.date(2025, 3, 1), 'quantity_sold': 500.0, 'price_per_tonne': 360.00},
        {'id': 12, 'harvest_id': 8, 'sale_date': datetime.date(2025, 3, 15), 'quantity_sold': 600.5, 'price_per_tonne': 362.40},
        {'id': 9, 'harvest_id': 9, 'sale_date': datetime.date(2025, 4, 15), 'quantity_sold': 5300.0, 'price_per_tonne': 180.50},
        {'id': 10, 'harvest_id': 11, 'sale_date': datetime.date(2025, 1, 25), 'quantity_sold': 8000.0, 'price_per_tonne': 230.00},
        {'id': 13, 'harvest_id': 12, 'sale_date': datetime.date(2025, 5, 15), 'quantity_sold': 5000.0, 'price_per_tonne': 298.00},
        {'id': 14, 'harvest_id': 12, 'sale_date': datetime.date(2025, 5, 28), 'quantity_sold': 7000.0, 'price_per_tonne': 301.50},
    ])


def downgrade() -> None:
    """Remove the initial seed data."""
    op.execute("DELETE FROM sales")
    op.execute("DELETE FROM harvests")
    op.execute("DELETE FROM crops")
    op.execute("DELETE FROM producers")