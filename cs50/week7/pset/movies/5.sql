/*
List the titles and release years of all Harry Potter movies, in
chronological order.
*/
SELECT m.title, m.year
  FROM movies AS m
 WHERE m.title LIKE 'Harry Potter%'
 ORDER BY m.year;
