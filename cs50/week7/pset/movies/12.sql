/*
List the titles of all movies in which both Bradley Cooper and Jennifer
Lawrence starred.
*/

SELECT title
  FROM movies AS m
       JOIN stars AS s
       ON m.id = s.movie_id

       JOIN people AS p
       ON s.person_id = p.id
 WHERE (SELECT id
         WHERE
       )
