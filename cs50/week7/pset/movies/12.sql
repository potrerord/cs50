/*
List the titles of all movies in which both Bradley Cooper and Jennifer
Lawrence starred.
*/
SELECT DISTINCT(title)
  FROM movies AS m
       INNER JOIN stars AS s
       ON m.id = s.movie_id

       INNER JOIN people AS p
       ON s.person_id = p.id
 WHERE p.name IN ('Bradley Cooper', 'Jennifer Lawrence')
 GROUP BY m.id;
