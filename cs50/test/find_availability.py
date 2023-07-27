"""
Locates Amazon warehouses that have a specific item in stock.
"""

from typing import Dict, List, Union

from cs50 import SQL

db = SQL("sqlite:///amazon.db")

def find_availability(item_id: int) -> List[Dict[int, Union[int, float]]]:
    """Return a list of dictionaries containing id, latitude, and
    longitude of warehouses stocking item_id.
    """

    # Get the id and location of relevant warehouses in database.
    available_warehouses = db.execute(
        """
        SELECT w.id, w.latitude, w.longitude
          FROM warehouses AS w
               INNER JOIN inventories AS inv
               ON w.id = inv.warehouse_id
         WHERE inv.item_id = ?
           AND inv.quantity > 0
        """,
        item_id
    )
