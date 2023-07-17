/*
List the titles of all movies in which both Bradley Cooper and Jennifer
Lawrence starred.
*/
SELECT movies.title
  FROM movies AS m
       INNER JOIN stars AS s
       ON m.id = s.movie_id

       INNER JOIN people AS p
       ON s.person_id = p.id
-- All movies starring either Bradley Cooper or Jennifer Lawrence
 WHERE p.name IN ('Bradley Cooper', 'Jennifer Lawrence')
 GROUP BY m.id  -- group the same movie
HAVING COUNT(m.id) > 1;  -- select the groups with both actors
