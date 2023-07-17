/*
List the names of all people who starred in a movie in which Kevin Bacon
also starred.
*/

SELECT name
  FROM people AS p
       JOIN stars AS s
       ON p.id = s.person_id

       JOIN movies AS m
       ON s.movie_id = m.id
 WHERE m.id IN
       -- Movies starring Kevin Bacon
       (SELECT s.movie_id
          FROM stars AS s
               JOIN people AS p
               ON s.person_id = p.id
         WHERE p.name = 'Kevin Bacon'
       )
   AND p.name != 'Kevin Bacon';
