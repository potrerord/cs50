"""
Locates Amazon warehouses that have a specific item in stock.
"""

from typing import Dict, List, Union

from cs50 import SQL

db = SQL("sqlite:///amazon.db")

def find_availability(item_id: int) -> List[Dict[int, Union[int, float]]]:
    """Return a list of warehouses in which an item with `item_id` is in
    stock."""

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
"""
-- Movie star names and IDs with matching movie IDs
SELECT p1.name
  FROM people AS p1
       INNER JOIN stars AS s1
       ON p1.id = s1.person_id
 WHERE s1.movie_id IN
       -- Movie IDs of movies starring Kevin Bacon
       (SELECT s2.movie_id
          FROM stars AS s2
               INNER JOIN people AS p2
               ON s2.person_id = p2.id
         WHERE p2.name = 'Kevin Bacon'
           AND p2.birth = 1958  -- Avoid other Kevin Bacons
       )
-- Exclude our Kevin Bacon from list (via id, not name)
   AND p1.id <>
       (SELECT p3.id
          FROM people AS p3
         WHERE p3.name = 'Kevin Bacon'
           AND p3.birth = 1958
       );"""