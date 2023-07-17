/*
List the titles of all movies with a release date on or after 2018,
in alphabetical order.
*/
SELECT m.title
  FROM movies AS m
 WHERE m.year >= 2018
 ORDER BY m.title;
