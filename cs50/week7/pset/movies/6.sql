/* Determine the average rating of all movies released in 2012. */
SELECT AVG(ratings.rating)
  FROM ratings AS r
       INNER JOIN movies AS m
       ON r.movie_id = m.id
 WHERE m.year = 2012;
