/*
List the titles of all movies in which both Bradley Cooper and Jennifer
Lawrence starred.
*/

SELECT DISTINCT(title)
  FROM movies AS m
       JOIN stars AS s
       ON m.id = s.movie_id

       JOIN people AS p
       ON s.person_id = p.id
          AND (p.name = 'Bradley Cooper'
               OR p.name = 'Jennifer Lawrence')

 -- Movie matches with both of the following:
 WHERE m.id IN
       -- Movies starring Bradley Cooper
       (SELECT id
         FROM movies AS m
              JOIN stars AS s
              ON m.id = s.movie_id

              JOIN people AS p
              ON s.person_id = p.id
        WHERE p.name = 'Bradley Cooper'
       )
   AND m.id IN
       -- Movies starring Jennifer Lawrence
       (SELECT id
         FROM movies AS m
              JOIN stars AS s
              ON m.id = s.movie_id

              JOIN people AS p
              ON s.person_id = p.id
        WHERE p.name = 'Jennifer Lawrence'
       );
