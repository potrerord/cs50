"""
Locates Amazon warehouses that have a specific item in stock.
"""

from typing import Dict, List, Union

from cs50 import SQL

db = SQL("sqlite:///amazon.db")

def find_availability(item_id: int) -> List[Dict[int, Union[int, float]]]:
    """Return a list of warehouses in which an item with `item_id` is in
    stock."""

    available_warehouses = db.execute(
        """
        SELECT *
          FROM warehouses AS w
               JOIN 
        """
    )

