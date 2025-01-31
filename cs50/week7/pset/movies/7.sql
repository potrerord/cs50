/*
List all movies released in 2010 and their ratings, in descending order
by rating. For movies with the same rating, order them alphabetically by
title.
*/
SELECT m.title, r.rating
  FROM movies AS m
       INNER JOIN ratings AS r  -- exclude movies with no ratings
       ON m.id = r.movie_id
 WHERE m.year = 2010
 ORDER BY rating DESC, title;
